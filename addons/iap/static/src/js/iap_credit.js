dosyt.define('iap.redirect_dosyt_credit_widget', function(require) {
"use strict";

var AbstractAction = require('web.AbstractAction');
var core = require('web.core');


var IapDosytCreditRedirect = AbstractAction.extend({
    template: 'iap.redirect_to_dosyt_credit',
    events : {
        "click .redirect_confirm" : "dosyt_redirect",
    },
    init: function (parent, action) {
        this._super(parent, action);
        this.url = action.params.url;
    },

    dosyt_redirect: function () {
        window.open(this.url, '_blank');
        this.do_action({type: 'ir.actions.act_window_close'});
        // framework.redirect(this.url);
    },

});
core.action_registry.add('iap_dosyt_credit_redirect', IapDosytCreditRedirect);
});
