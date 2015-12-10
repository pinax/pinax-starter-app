import pkg_resources


default_app_config = "pinax.{{ app_name }}.apps.AppConfig"
__version__ = pkg_resources.get_distribution("pinax-{{ app_name }}").version
