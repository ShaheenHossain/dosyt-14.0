# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import fields, models
from dosyt.tools.translate import _


class MailingList(models.Model):
    _inherit = 'mailing.list'

    def _default_toast_content(self):
        return _('<p>Thanks for subscribing!</p>')

    website_popup_ids = fields.One2many('website.mass_mailing.popup', 'mailing_list_id', string="Website Popups")
    toast_content = fields.Html(default=_default_toast_content, translate=True)
