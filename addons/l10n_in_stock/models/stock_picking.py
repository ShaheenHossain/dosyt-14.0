# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def _should_generate_commercial_invoice(self):
        super(StockPicking, self)._should_generate_commercial_invoice()
        return True
