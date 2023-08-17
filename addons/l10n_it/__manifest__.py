# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

{
    'name': 'Italy - Accounting',
    'version': '0.2',
    'depends': [
        'account',
        'base_iban',
        'base_vat',
    ],
    'author': 'OpenERP Italian Community',
    'description': """
Piano dei conti italiano di un'impresa generica.
================================================

Italian accounting chart and localization.
    """,
    'category': 'Accounting/Localizations/Account Charts',
    'website': 'http://www.dosyt.com/',
    'data': [
        'data/l10n_it_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.tax.group.csv',
        'data/account_tax_report_data.xml',
        'data/account_tax_template.xml',
        'data/account.fiscal.position.template.csv',
        'data/account.chart.template.csv',
        'data/account_fiscal_position_tax_template_data.xml',
        'data/account_chart_template_data.xml',
        'data/report_invoice.xml'
    ],
    'demo': [
        'demo/demo_company.xml',
    ],
    'license': 'LGPL-3',
}
