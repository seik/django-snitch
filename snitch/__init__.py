"""Django app made to integrate generic events that create notifications that
can be sent to users using several backends.

By default, it integrates push notifications and email to send the
notifications.
"""
from django.utils.module_loading import autodiscover_modules

from snitch.decorators import register, dispatch
from snitch.handlers import manager, EventHandler
from snitch.helpers import explicit_dispatch, get_notification_model


__all__ = [
    "register",
    "manager",
    "EventHandler",
    "dispatch",
    "explicit_dispatch",
    "get_notification_model",
]

__version__ = "1.2.1"


def autodiscover():
    autodiscover_modules("events", register_to=manager)


default_app_config = "snitch.apps.SnitchConfig"
