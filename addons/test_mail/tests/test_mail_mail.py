# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

import psycopg2

from dosyt import api
from dosyt.addons.test_mail.tests.common import TestMailCommon
from dosyt.tests import common, tagged
from dosyt.tools import mute_logger


@tagged('mail_mail')
class TestMailMail(TestMailCommon):

    @classmethod
    def setUpClass(cls):
        super(TestMailMail, cls).setUpClass()
        cls._init_mail_gateway()

        cls.test_record = cls.env['mail.test.gateway'].with_context(cls._test_context).create({
            'name': 'Test',
            'email_from': 'ignasse@example.com',
        }).with_context({})

    @mute_logger('dosyt.addons.mail.models.mail_mail')
    def test_mail_message_notify_from_mail_mail(self):
        # Due ot post-commit hooks, store send emails in every step
        mail = self.env['mail.mail'].sudo().create({
            'body_html': '<p>Test</p>',
            'email_to': 'test@example.com',
            'partner_ids': [(4, self.user_employee.partner_id.id)]
        })
        with self.mock_mail_gateway():
            mail.send()
        self.assertSentEmail(mail.env.user.partner_id, ['test@example.com'])
        self.assertEqual(len(self._mails), 1)

    def test_mail_mail_return_path(self):
        # mail without thread-enabled record
        base_values = {
            'body_html': '<p>Test</p>',
            'email_to': 'test@example.com',
        }

        mail = self.env['mail.mail'].create(base_values)
        with self.mock_mail_gateway():
            mail.send()
        self.assertEqual(self._mails[0]['headers']['Return-Path'], '%s+%d@%s' % (self.alias_bounce, mail.id, self.alias_domain))

        # mail on thread-enabled record
        mail = self.env['mail.mail'].create(dict(base_values, **{
            'model': self.test_record._name,
            'res_id': self.test_record.id,
        }))
        with self.mock_mail_gateway():
            mail.send()
        self.assertEqual(self._mails[0]['headers']['Return-Path'], '%s+%d-%s-%s@%s' % (self.alias_bounce, mail.id, self.test_record._name, self.test_record.id, self.alias_domain))

        # force static addressing on bounce alias
        self.env['ir.config_parameter'].set_param('mail.bounce.alias.static', True)

        # mail without thread-enabled record
        mail = self.env['mail.mail'].create(base_values)
        with self.mock_mail_gateway():
            mail.send()
        self.assertEqual(self._mails[0]['headers']['Return-Path'], '%s@%s' % (self.alias_bounce, self.alias_domain))

        # mail on thread-enabled record
        mail = self.env['mail.mail'].create(dict(base_values, **{
            'model': self.test_record._name,
            'res_id': self.test_record.id,
        }))
        with self.mock_mail_gateway():
            mail.send()
        self.assertEqual(self._mails[0]['headers']['Return-Path'], '%s@%s' % (self.alias_bounce, self.alias_domain))


class TestMailMailRace(common.TransactionCase):

    @mute_logger('dosyt.addons.mail.models.mail_mail')
    def test_mail_bounce_during_send(self):
        self.partner = self.env['res.partner'].create({
            'name': 'Ernest Partner',
        })
        # we need to simulate a mail sent by the cron task, first create mail, message and notification by hand
        mail = self.env['mail.mail'].sudo().create({
            'body_html': '<p>Test</p>',
            'notification': True,
            'state': 'outgoing',
            'recipient_ids': [(4, self.partner.id)]
        })
        message = self.env['mail.message'].create({
            'subject': 'S',
            'body': 'B',
            'subtype_id': self.ref('mail.mt_comment'),
            'notification_ids': [(0, 0, {
                'res_partner_id': self.partner.id,
                'mail_id': mail.id,
                'notification_type': 'email',
                'is_read': True,
                'notification_status': 'ready',
            })],
        })
        notif = self.env['mail.notification'].search([('res_partner_id', '=', self.partner.id)])
        # we need to commit transaction or cr will keep the lock on notif
        self.cr.commit()

        # patch send_email in order to create a concurent update and check the notif is already locked by _send()
        this = self  # coding in javascript ruinned my life
        bounce_deferred = []
        @api.model
        def send_email(self, message, *args, **kwargs):
            with this.registry.cursor() as cr, mute_logger('dosyt.sql_db'):
                try:
                    # try ro aquire lock (no wait) on notification (should fail)
                    cr.execute("SELECT notification_status FROM mail_message_res_partner_needaction_rel WHERE id = %s FOR UPDATE NOWAIT", [notif.id])
                except psycopg2.OperationalError:
                    # record already locked by send, all good
                    bounce_deferred.append(True)
                else:
                    # this should trigger psycopg2.extensions.TransactionRollbackError in send().
                    # Only here to simulate the initial use case
                    # If the record is lock, this line would create a deadlock since we are in the same thread
                    # In practice, the update will wait the end of the send() transaction and set the notif as bounce, as expeced
                    cr.execute("UPDATE mail_message_res_partner_needaction_rel SET notification_status='bounce' WHERE id = %s", [notif.id])
            return message['Message-Id']
        self.env['ir.mail_server']._patch_method('send_email', send_email)

        mail.send()

        self.assertTrue(bounce_deferred, "The bounce should have been deferred")
        self.assertEqual(notif.notification_status, 'sent')

        # some cleaning since we commited the cr
        self.env['ir.mail_server']._revert_method('send_email')

        notif.unlink()
        message.unlink()
        mail.unlink()
        self.partner.unlink()
        self.env.cr.commit()
