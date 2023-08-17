# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import models, _


class MailBot(models.AbstractModel):
    _inherit = 'mail.bot'

    def _get_answer(self, record, body, values, command):
        dosytbot_state = self.env.user.dosytbot_state
        if self._is_bot_in_private_channel(record):
            if dosytbot_state == "onboarding_attachement" and values.get("attachment_ids"):
                self.env.user.dosytbot_failed = False
                self.env.user.dosytbot_state = "onboarding_canned"
                return _("That's me! 🎉<br/>Try typing <span class=\"o_dosytbot_command\">:</span> to use canned responses.")
            elif dosytbot_state == "onboarding_canned" and values.get("canned_response_ids"):
                self.env.user.dosytbot_failed = False
                self.env.user.dosytbot_state = "idle"
                return _("Good, you can customize canned responses in the live chat application.<br/><br/><b>It's the end of this overview</b>, enjoy discovering Dosyt!")
            # repeat question if needed
            elif dosytbot_state == 'onboarding_canned' and not self._is_help_requested(body):
                self.env.user.dosytbot_failed = True
                return _("Not sure what you are doing. Please, type <span class=\"o_dosytbot_command\">:</span> and wait for the propositions. Select one of them and press enter.")
        return super(MailBot, self)._get_answer(record, body, values, command)
