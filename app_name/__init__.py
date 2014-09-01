import pkg_resources


__version__ = pkg_resources.get_distribution("django-{{ app_name }}").version
