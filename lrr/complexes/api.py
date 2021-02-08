# -*- coding: utf-8 -*-
from rest_framework import viewsets, permissions

from lrr.complexes import models
from lrr.complexes import serializers


class DigitalComplexViewSet(viewsets.ModelViewSet):
    """ViewSet for the Status_COR class"""

    queryset = models.DigitalComplex.objects.all()
    serializer_class = serializers.DigitalComplexSerializer
    permission_classes = [permissions.IsAuthenticated]


class CellViewSet(viewsets.ModelViewSet):
    """ViewSet for the Expertise_status class"""

    queryset = models.Cell.objects.all()
    serializer_class = serializers.CellSerializer
    permission_classes = [permissions.IsAuthenticated]


class ComplexSpaceCellViewSet(viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.ComplexSpaceCell.objects.all()
    serializer_class = serializers.ComplexSpaceCellSerializer
    permission_classes = [permissions.IsAuthenticated]


class WorkPlanAcademicGroupViewSet(viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.AssignmentAcademicGroup.objects.all()
    serializer_class = serializers.WorkPlanAcademicGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
