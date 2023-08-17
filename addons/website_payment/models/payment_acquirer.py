# coding: utf-8

from dosyt import fields, models


class PaymentAcquirer(models.Model):
    _inherit = "payment.acquirer"

    website_id = fields.Many2one(
        "website",
        domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        ondelete="restrict",
    )
