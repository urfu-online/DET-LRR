# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .survey import Survey
import auto_prefetch

try:
    from django.conf import settings

    if settings.AUTH_USER_MODEL:
        user_model = settings.AUTH_USER_MODEL
    else:
        user_model = User
except (ImportError, AttributeError):
    user_model = User


class Response(auto_prefetch.Model):
    """
    A Response object is a collection of questions and answers with a
    unique interview uuid.
    """

    created = models.DateTimeField(_("Creation date"), auto_now_add=True)
    updated = models.DateTimeField(_("Update date"), auto_now=True)
    survey = auto_prefetch.ForeignKey(Survey, on_delete=models.CASCADE, verbose_name="Вид экспертизы", related_name="responses")
    expertise_opinion = auto_prefetch.ForeignKey('inspections.ExpertiseOpinion', on_delete=models.CASCADE,
                                                 verbose_name="Экспертное заключение", related_name='requests', blank=True,
                                                 null=True)
    user = models.ForeignKey(user_model, on_delete=models.SET_NULL, verbose_name=_("User"), null=True, blank=True)
    interview_uuid = models.CharField(_("Interview unique identifier"), max_length=36)

    class Meta:
        verbose_name = "показатель заключения"
        verbose_name_plural = "показатели заключения"
        get_latest_by = "created"

    def __str__(self):
        msg = "Показатель заключения to {} by {}".format(self.survey, self.user)
        msg += " on {}".format(self.created)
        return msg
