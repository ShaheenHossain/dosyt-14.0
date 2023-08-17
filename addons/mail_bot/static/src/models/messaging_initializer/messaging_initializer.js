dosyt.define('mail_bot/static/src/models/messaging_initializer/messaging_initializer.js', function (require) {
'use strict';

const { registerInstancePatchModel } = require('mail/static/src/model/model_core.js');

registerInstancePatchModel('mail.messaging_initializer', 'mail_bot/static/src/models/messaging_initializer/messaging_initializer.js', {
    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    async _initializeDosytBot() {
        const data = await this.async(() => this.env.services.rpc({
            model: 'mail.channel',
            method: 'init_dosytbot',
        }));
        if (!data) {
            return;
        }
        this.env.session.dosytbot_initialized = true;
    },

    /**
     * @override
     */
    async start() {
        await this.async(() => this._super());

        if ('dosytbot_initialized' in this.env.session && !this.env.session.dosytbot_initialized) {
            this._initializeDosytBot();
        }
    },
});

});
