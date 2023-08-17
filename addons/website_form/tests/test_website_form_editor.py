# Part of Dosyt. See LICENSE file for full copyright and licensing details.
# -*- coding: utf-8 -*-

import dosyt.tests


@dosyt.tests.tagged('post_install','-at_install')
class TestWebsiteFormEditor(dosyt.tests.HttpCase):
    def test_tour(self):
        self.start_tour("/", 'website_form_editor_tour', login="admin")
        self.start_tour("/", 'website_form_editor_tour_submit')
        self.start_tour("/", 'website_form_editor_tour_results', login="admin")
