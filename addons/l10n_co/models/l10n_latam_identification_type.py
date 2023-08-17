# Part of Dosyt. See LICENSE file for full copyright and licensing details.
from dosyt import models, fields


class L10nCoDocumentType(models.Model):
    _inherit = "l10n_latam.identification.type"

    l10n_co_document_code = fields.Char("Document Code")