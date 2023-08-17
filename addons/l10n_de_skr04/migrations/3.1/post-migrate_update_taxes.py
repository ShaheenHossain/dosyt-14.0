# Part of Dosyt. See LICENSE file for full copyright and licensing details.
from dosyt.addons.account.models.chart_template import update_taxes_from_templates


def migrate(cr, version):
    update_taxes_from_templates(cr, 'l10n_de_skr04.l10n_chart_de_skr04')
