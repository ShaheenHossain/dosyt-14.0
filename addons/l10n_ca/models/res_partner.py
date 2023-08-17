# coding: utf-8
from dosyt import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    l10n_ca_pst = fields.Char('PST')
