# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import models
from dosyt.modules.loading import force_demo
from dosyt.addons.base.models.ir_module import assert_log_admin_access


class IrDemo(models.TransientModel):

    _name = 'ir.demo'
    _description = 'Demo'

    @assert_log_admin_access
    def install_demo(self):
        force_demo(self.env.cr)
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': '/web',
        }
