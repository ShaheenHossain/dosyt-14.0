# Part of Dosyt. See LICENSE file for full copyright and licensing details.

import dosyt.tests


@dosyt.tests.tagged('post_install', '-at_install')
class TestUi(dosyt.tests.HttpCase):

    def test_01_mail_tour(self):
        self.start_tour("/web", 'mail_tour', login="admin")
