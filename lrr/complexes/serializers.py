# -*- coding: utf-8 -*-
import logging

from rest_framework import serializers

from lrr.complexes import models as complexes_models
from lrr.repository import serializers as repo_serializers

logger = logging.getLogger(__name__)


class WorkPlanAcademicGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = complexes_models.AssignmentAcademicGroup
        fields = [
            "academic_group",
            "learn_date",
            "direction",
            "subject"
        ]


class CellSerializer(serializers.ModelSerializer):
    class Meta:
        model = complexes_models.ComplexSpaceCell
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


class DigitalComplexSerializer(serializers.ModelSerializer):
    subjects = repo_serializers.SubjectSerializer(many=True, read_only=True)
    competences = repo_serializers.CompetenceSerializer(many=True, read_only=True)
    results_edu = repo_serializers.ResultEduSerializer(many=True, read_only=True)
    directions = repo_serializers.DirectionSerializer(many=True, read_only=True)
    digital_resources = repo_serializers.DigitalResourceSerializer(many=True, read_only=True)
    complex_space_cell = ComplexSpaceCellSerializer(many=False, read_only=True)
    works_plans_academic = WorkPlanAcademicGroupSerializer(many=True, read_only=True)

    class Meta:
        model = complexes_models.DigitalComplex
        fields = [
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
            "works_plans_academic"
        ]
