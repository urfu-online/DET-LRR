# -*- coding: utf-8 -*-
from rest_framework import viewsets, permissions

from lrr.inspections import models
from lrr.inspections import serializers


class ExpertiseViewSet(viewsets.ModelViewSet):
    """ViewSet for the Status_COR class"""

    queryset = models.Expertise.objects.all()
    serializer_class = serializers.ExpertiseSerializer
    permission_classes = [permissions.IsAuthenticated]


class CheckListViewSet(viewsets.ModelViewSet):
    """ViewSet for the Expertise_status class"""

    queryset = models.ExpertiseRequest.objects.all()
    serializer_class = serializers.CheckListSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.Question.objects.all()
    serializer_class = serializers.QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
