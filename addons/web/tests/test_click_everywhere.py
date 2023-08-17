# Part of Dosyt. See LICENSE file for full copyright and licensing details.

import logging
import dosyt.tests

_logger = logging.getLogger(__name__)


@dosyt.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusAdmin(dosyt.tests.HttpCase):

    def test_01_click_everywhere_as_admin(self):
        menus = self.env['ir.ui.menu'].load_menus(False)
        for app in menus['children']:
                with self.subTest(app=app['name']):
                    _logger.runbot('Testing %s', app['name'])
                    self.browser_js("/web", "dosyt.__DEBUG__.services['web.clickEverywhere']('%s');" % app['xmlid'], "dosyt.isReady === true", login="admin", timeout=300)
                    self.terminate_browser()


@dosyt.tests.tagged('click_all', 'post_install', '-at_install', '-standard')
class TestMenusDemo(dosyt.tests.HttpCase):

    def test_01_click_everywhere_as_demo(self):
        menus = self.env['ir.ui.menu'].load_menus(False)
        for app in menus['children']:
                with self.subTest(app=app['name']):
                    _logger.runbot('Testing %s', app['name'])
                    self.browser_js("/web", "dosyt.__DEBUG__.services['web.clickEverywhere']('%s');" % app['xmlid'], "dosyt.isReady === true", login="demo", timeout=300)
                    self.terminate_browser()

@dosyt.tests.tagged('post_install', '-at_install')
class TestMenusAdminLight(dosyt.tests.HttpCase):

    def test_01_click_apps_menus_as_admin(self):
        self.browser_js("/web", "dosyt.__DEBUG__.services['web.clickEverywhere'](undefined, true);", "dosyt.isReady === true", login="admin", timeout=120)

@dosyt.tests.tagged('post_install', '-at_install',)
class TestMenusDemoLight(dosyt.tests.HttpCase):

    def test_01_click_apps_menus_as_demo(self):
            self.browser_js("/web", "dosyt.__DEBUG__.services['web.clickEverywhere'](undefined, true);", "dosyt.isReady === true", login="demo", timeout=120)
