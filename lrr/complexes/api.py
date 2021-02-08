# -*- coding: utf-8 -*-
import logging
from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from lrr.complexes import models
from lrr.repository.models import DigitalResource, Subject
from lrr.complexes import serializers
from lrr.repository.serializers import DigitalResourceSerializer
from lrr.users.mixins import GroupRequiredMixin
from lrr.inspections.models import Expertise

from lrr.users.models import Student

logger = logging.getLogger(__name__)


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


class AssignmentAcademicGroupComplexListViewSet(GroupRequiredMixin, viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.AssignmentAcademicGroup.objects.all()
    serializer_class = serializers.AssignmentAcademicComplexListGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['academic_group__direction', 'subject', 'semestr', 'learn_date']
    group_required = ['student', 'admins']

    def get_queryset(self):
        user = self.request.user
        academic_group = Student.get_academic_group_for_user(user)
        queryset = models.AssignmentAcademicGroup.objects.filter(academic_group=academic_group)
        return queryset


class ComponentsSerializer(GroupRequiredMixin, viewsets.ModelViewSet):
    queryset = models.ComponentComplex.objects.all()
    serializer_class = serializers.ComponentsPolymorphicSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['polymorphic_ctype']
    group_required = ['student', 'admins']


class ResourceAssignedStatusTag(GroupRequiredMixin, viewsets.ModelViewSet):
    queryset = models.AssignmentAcademicGroup.objects.all()
    serializer_class = serializers.AssignmentAcademicResourceListGroupSerializer
    group_required = ['student', 'admins']

    # def get_queryset(self, **kwargs):
    #     subject = Subject.objects.get(title='Радиосистемы и комплексы управления')
    #     queryset = DigitalResource.get_resources_by_subject(subject)
    #     return queryset
# class RecomentedDigitalComplexSerializer(GroupRequiredMixin, viewsets.ModelViewSet):
#
#     queryset = DigitalResource.objects.all()
#     serializer_class = DigitalResourceSerializer
#     permission_classes = [permissions.IsAuthenticated]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['academic_group__direction', 'subject', 'semestr', 'learn_date']
