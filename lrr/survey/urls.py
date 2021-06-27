# -*- coding: utf-8 -*-

from django.conf.urls import url

from lrr.survey.views import ConfirmView, IndexView, SurveyCompleted, SurveyDetail
from lrr.survey.views.survey_result import serve_result_csv

urlpatterns = [
    url(r"^$", IndexView.as_view(), name="survey-list"),
    # path("survey/<id:id>/<uuid:uuid_pk>/", SurveyDetail.as_view(), name="survey-detail"),
    url(r"^(?P<id>\d+)/(?P<expertise_request_pk>[0-9a-f-]+)/", SurveyDetail.as_view(), name="survey-detail"),
    url(r"^csv/(?P<primary_key>\d+)/", serve_result_csv, name="survey-result"),
    url(r"^(?P<id>\d+)/completed/", SurveyCompleted.as_view(), name="survey-completed"),
    url(r"^(?P<id>\d+)-(?P<step>\d+)/", SurveyDetail.as_view(), name="survey-detail-step"),
    url(r"^confirm/(?P<uuid>\w+)/", ConfirmView.as_view(), name="survey-confirmation"),
]
