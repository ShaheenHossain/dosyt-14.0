# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import models
from dosyt.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        user = request.env.user
        result = super(IrHttp, self).session_info()
        if self.env.user.has_group('base.group_user'):
            result['notification_type'] = user.notification_type
        return result
