# -*- coding: utf-8 -*-

import dosyt

def migrate(cr, version):
    registry = dosyt.registry(cr.dbname)
    from dosyt.addons.account.models.chart_template import migrate_set_tags_and_taxes_updatable
    migrate_set_tags_and_taxes_updatable(cr, registry, 'l10n_hr')
