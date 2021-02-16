# -*- coding: utf-8 -*-
import logging

from rest_framework import serializers
from rest_polymorphic.serializers import PolymorphicSerializer

from lrr.complexes import models as complexes_models
from lrr.repository import serializers as repo_serializers

# from lrr.users.models import AcademicGroup

logger = logging.getLogger(__name__)


# class AcademicGroupSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AcademicGroup
#         fields = [
#             "academic_group",
#             "direction",
#         ]


class ResourceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = complexes_models.DigitalResource
        fields = [
            "title",
            "pk",
        ]


class AssignmentAcademicResourceListGroupSerializer(serializers.ModelSerializer):
    direction = serializers.CharField(source='academic_group.direction')
    academic_group = serializers.CharField(source='academic_group.number')
    subject = serializers.CharField(source='subject.title')
    digital_resource = ResourceListSerializer(read_only=True, many=True)

    class Meta:
        model = complexes_models.AssignmentAcademicGroup
        fields = [
            "digital_resource",
            "academic_group",
            "learn_date",
            "direction",
            "subject",
            "semestr",
        ]


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = complexes_models.Cell
        fields = [
            "type",
            "include_practice",
            "include_theory",
            "beg_theme_number",
            "end_theme_number",
            "methodology_description",
        ]


class ComplexSpaceCellSerializer(serializers.ModelSerializer):
    cells = CellSerializer(many=True, read_only=True)

    class Meta:
        model = complexes_models.ComplexSpaceCell
        fields = [
            "title",
            "description",
            "link",
            "cells",
        ]


class AssignmentAcademicComplexListGroupSerializer(serializers.ModelSerializer):
    direction = serializers.CharField(source='academic_group.direction')
    academic_group = serializers.CharField(source='academic_group.number')
    subject = serializers.CharField(source='subject.title')
    subject_pk = serializers.CharField(source='subject.pk')
    digital_complex_pk = serializers.CharField(source='digital_complex.pk')
    digital_complex_title = serializers.CharField(source='digital_complex.title')
    digital_complex_format = serializers.CharField(source='digital_complex.format')
    digital_complex_keywords = serializers.CharField(source='digital_complex.keywords')

    class Meta:
        model = complexes_models.AssignmentAcademicGroup
        fields = [
            "digital_complex_pk",
            "digital_complex_title",
            "digital_complex_format",
            "digital_complex_keywords",
            "academic_group",
            "learn_date",
            "direction",
            "subject",
            "subject_pk",
            "semestr",
        ]


class DigitalComplexSerializer(serializers.ModelSerializer):
    subjects = repo_serializers.SubjectSerializer(many=True, read_only=True)
    competences = repo_serializers.CompetenceSerializer(many=True, read_only=True)
    results_edu = repo_serializers.ResultEduSerializer(many=True, read_only=True)
    directions = repo_serializers.DirectionSerializer(many=True, read_only=True)
    digital_resources = repo_serializers.DigitalResourceSerializer(many=True, read_only=True)
    complex_space_cell = ComplexSpaceCellSerializer(many=False, read_only=True)
    assignment_group = AssignmentAcademicComplexListGroupSerializer(many=True, read_only=True)

    class Meta:
        model = complexes_models.DigitalComplex
        fields = [
            "title",
            "keywords",
            "description",
            "language",
            "format",
            "subjects",
            "directions",
            "competences",
            "results_edu",
            "digital_resources",
            "complex_space_cell",
            "assignment_group",
            "owner"
        ]


class ComponentComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = complexes_models.ComponentComplex
        fields = '__all__'


class ResourceComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = complexes_models.ResourceComponent
        fields = '__all__'


class PlatformComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = complexes_models.PlatformComponent
        fields = '__all__'


class TraditionalSessionComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = complexes_models.TraditionalSessionComponent
        fields = '__all__'


class ComponentsPolymorphicSerializer(PolymorphicSerializer):
    model_serializer_mapping = {
        complexes_models.ComponentComplex: ComponentComplexSerializer,
        complexes_models.ResourceComponent: ResourceComponentSerializer,
        complexes_models.PlatformComponent: PlatformComponentSerializer,
        complexes_models.TraditionalSessionComponent: TraditionalSessionComponentSerializer
    }
