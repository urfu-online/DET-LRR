from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class RepositoryConfig(AppConfig):
    name = "lrr.repository"
    verbose_name = _("Digital resources repository")
