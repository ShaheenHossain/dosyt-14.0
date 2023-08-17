# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import models, fields, api


class Stock(models.Model):
    _inherit = 'stock.warehouse'

    l10n_in_sale_journal_id = fields.Many2one('account.journal', string="Sale Journal")
