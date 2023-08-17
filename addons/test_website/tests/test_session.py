import dosyt.tests
from dosyt.tools import mute_logger


@dosyt.tests.common.tagged('post_install', '-at_install')
class TestWebsiteSession(dosyt.tests.HttpCase):

    def test_01_run_test(self):
        self.start_tour('/', 'test_json_auth')
