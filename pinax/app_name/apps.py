import importlib

from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.{{ app_name }}"
    label = "pinax_{{ app_name }}"
    verbose_name = _("Pinax {{ app_name|title }}")
