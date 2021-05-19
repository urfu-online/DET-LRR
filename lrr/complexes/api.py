# -*- coding: utf-8 -*-
import logging
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import viewsets, permissions

from lrr.complexes import grid_models
from lrr.complexes import models
from lrr.complexes import serializers
from lrr.inspections.models import Expertise
from lrr.inspections.serializers import ExpertiseSubjectListSerializer
from lrr.repository.models import DigitalResource
from lrr.repository.serializers import DigitalResourceListSerializer
from lrr.users.mixins import GroupRequiredMixin
from lrr.users.models import Student

logger = logging.getLogger(__name__)


class DigitalComplexViewSet(viewsets.ModelViewSet):
    """ViewSet for the Status_COR class"""

    queryset = models.DigitalComplex.objects.all()
    serializer_class = serializers.DigitalComplexSerializer
    permission_classes = [permissions.IsAuthenticated]


class CellViewSet(viewsets.ModelViewSet):
    """ViewSet for the Expertise_status class"""

    queryset = grid_models.Cell.objects.all()
    serializer_class = serializers.CellSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssignmentAcademicGroupComplexListViewSet(GroupRequiredMixin, viewsets.ModelViewSet):
    """ViewSet for the Subject class"""

    queryset = models.AssignmentAcademicGroup.objects.all()
    serializer_class = serializers.AssignmentAcademicComplexListGroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['academic_group__eduprogram', 'subject__title', 'semestr', 'learn_date']
    group_required = ['student', 'admins']

    def get_queryset(self):
        user = self.request.user
        academic_group = Student.get_academic_group_for_user(user)
        queryset = models.AssignmentAcademicGroup.objects.filter(academic_group=academic_group)
        return queryset


class DigitalResourceFilter(FilterSet):
    subjects = filters.Filter(field_name="subjects_tags__tag__title")

    class Meta:
        model = DigitalResource
        fields = ['title', 'subjects']


class DigitalResourceSubjectListViewSet(viewsets.ModelViewSet):
    """ViewSet for the DigitalResource class"""

    queryset = DigitalResource.objects.all()
    serializer_class = DigitalResourceListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DigitalResourceFilter

    # def get_queryset(self):
    #     # project_id may be None
    #     return self.queryset \
    #         .filter(project_id=self.kwargs.get('project_id')) \
    #         .filter(author=self.request.user)


class DigitalResourceSubjectListRecomendedFilter(FilterSet):
    subjects = filters.Filter(field_name="digital_resource__subjects_tags__tag__title")

    class Meta:
        model = Expertise
        fields = ['subjects']


class DigitalResourceSubjectListRecomended(viewsets.ModelViewSet):
    queryset = Expertise.objects.filter(status='ASSIGNED_STATUS')
    serializer_class = ExpertiseSubjectListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DigitalResourceSubjectListRecomendedFilter


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
