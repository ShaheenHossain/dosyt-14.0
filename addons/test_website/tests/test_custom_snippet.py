# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

import dosyt.tests
from dosyt.tools import mute_logger


@dosyt.tests.common.tagged('post_install', '-at_install')
class TestCustomSnippet(dosyt.tests.HttpCase):

    @mute_logger('dosyt.addons.http_routing.models.ir_http', 'dosyt.http')
    def test_01_run_tour(self):
        self.start_tour("/", 'test_custom_snippet', login="admin")
