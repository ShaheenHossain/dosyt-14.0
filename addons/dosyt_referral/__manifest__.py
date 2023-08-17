# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.
{
    'name': "Dosyt referral program",
    'summary': """Allow you to refer your friends to Dosyt and get rewards""",
    'category': 'Hidden',
    'version': '1.0',
    'depends': ['base', 'web'],
    'data': [
        'views/templates.xml',
    ],
    'qweb': [
        "static/src/xml/systray.xml",
    ],
    'auto_install': False,
    'license': 'LGPL-3',
}
