# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    plan_to_change_car = fields.Boolean('Plan To Change Car', default=False)
