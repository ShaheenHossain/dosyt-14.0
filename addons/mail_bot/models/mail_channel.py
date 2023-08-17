# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import api, models, _


class Channel(models.Model):
    _inherit = 'mail.channel'

    def _execute_command_help(self, **kwargs):
        super(Channel, self)._execute_command_help(**kwargs)
        self.env['mail.bot']._apply_logic(self, kwargs, command="help")  # kwargs are not usefull but...

    @api.model
    def init_dosytbot(self):
        if self.env.user.dosytbot_state in [False, 'not_initialized']:
            dosytbot_id = self.env['ir.model.data'].xmlid_to_res_id("base.partner_root")
            channel_info = self.channel_get([dosytbot_id])
            channel = self.browse(channel_info['id'])
            message = _("Hello,<br/>Dosyt's chat helps employees collaborate efficiently. I'm here to help you discover its features.<br/><b>Try to send me an emoji</b> <span class=\"o_dosytbot_command\">:)</span>")
            channel.sudo().message_post(body=message, author_id=dosytbot_id, message_type="comment", subtype_xmlid="mail.mt_comment")
            self.env.user.dosytbot_state = 'onboarding_emoji'
            return channel
