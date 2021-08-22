# -*- coding: utf-8 -*-

import auto_prefetch
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from .survey import Survey


class Category(auto_prefetch.Model):
    name = models.CharField(_("Name"), max_length=400)
    survey = auto_prefetch.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name=_("Survey"), related_name="categories",
                                      null=True, blank=True)
    order = models.IntegerField(_("Display order"), blank=True, null=True)
    description = models.CharField(_("Description"), max_length=2000, blank=True, null=True)

    class Meta:
        # pylint: disable=too-few-public-methods
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return self.name

    def slugify(self):
        return slugify(str(self), allow_unicode=True)
