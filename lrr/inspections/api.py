# -*- coding: utf-8 -*-
from rest_framework import viewsets, permissions

from lrr.inspections import models
from lrr.inspections import serializers


class RequestViewSet(viewsets.ModelViewSet):
    """ViewSet for the Status_COR class"""

    queryset = models.Request.objects.all()
    serializer_class = serializers.RequestSerializer
    permission_classes = [permissions.IsAuthenticated]


class CheckListViewSet(viewsets.ModelViewSet):
    """ViewSet for the Expertise_status class"""

    queryset = models.ExpertiseOpinion.objects.all()
    serializer_class = serializers.CheckListSerializer
    permission_classes = [permissions.IsAuthenticated]
