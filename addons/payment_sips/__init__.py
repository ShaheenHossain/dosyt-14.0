from . import models
from . import controllers
from dosyt.addons.payment.models.payment_acquirer import create_missing_journal_for_acquirers
from dosyt.addons.payment import reset_payment_provider

def uninstall_hook(cr, registry):
    reset_payment_provider(cr, registry, 'sips')
