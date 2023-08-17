# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

import dosyt.tests
from dosyt import tools


@dosyt.tests.tagged('post_install', '-at_install')
class TestUi(dosyt.tests.HttpCase):
    def test_admin(self):
        self.start_tour("/", 'event', login='admin', step_delay=100)
