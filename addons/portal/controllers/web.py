# -*- coding: utf-8 -*-
# Part of Dosyt. See LICENSE file for full copyright and licensing details.

from dosyt import http
from dosyt.addons.web.controllers.main import Home
from dosyt.http import request


class Home(Home):

    @http.route()
    def index(self, *args, **kw):
        if request.session.uid and not request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_user'):
            return http.local_redirect('/my', query=request.params, keep_hash=True)
        return super(Home, self).index(*args, **kw)

    def _login_redirect(self, uid, redirect=None):
        if not redirect and not request.env['res.users'].sudo().browse(uid).has_group('base.group_user'):
            redirect = '/my'
        return super(Home, self)._login_redirect(uid, redirect=redirect)

    @http.route('/web', type='http', auth="none")
    def web_client(self, s_action=None, **kw):
        if request.session.uid and not request.env['res.users'].sudo().browse(request.session.uid).has_group('base.group_user'):
            return http.local_redirect('/my', query=request.params, keep_hash=True)
        return super(Home, self).web_client(s_action, **kw)
