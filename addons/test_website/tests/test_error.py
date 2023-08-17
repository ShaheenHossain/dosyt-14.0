import dosyt.tests
from dosyt.tools import mute_logger


@dosyt.tests.common.tagged('post_install', '-at_install')
class TestWebsiteError(dosyt.tests.HttpCase):

    @mute_logger('dosyt.addons.http_routing.models.ir_http', 'dosyt.http')
    def test_01_run_test(self):
        self.start_tour("/test_error_view", 'test_error_website')
