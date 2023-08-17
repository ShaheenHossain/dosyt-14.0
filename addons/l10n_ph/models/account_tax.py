# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import fields, models


class AccountTax(models.Model):
    _inherit = "account.tax"

    l10n_ph_atc = fields.Char("Philippines ATC")
