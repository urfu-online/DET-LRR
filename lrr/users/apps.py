from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "lrr.users"
    verbose_name = _("Users")
    label = "users"

    def ready(self):
        try:
            import lrr.users.signals  # noqa F401
        except ImportError:
            pass
