# Part of Dosyt. See LICENSE file for full copyright and licensing details.
from dosyt.addons.point_of_sale.controllers.main import PosController
from dosyt import http
from dosyt.http import request


class PosCache(PosController):

    @http.route()
    def load_onboarding_data(self):
        super().load_onboarding_data()
        request.env["pos.cache"].refresh_all_caches()
