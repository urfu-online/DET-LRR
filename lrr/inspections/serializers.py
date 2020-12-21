# -*- coding: utf-8 -*-
import logging

from rest_framework import serializers

from lrr.inspections import models as inspections_models
from lrr.repository import serializers as repo_serializers

logger = logging.getLogger(__name__)


class ExpertiseSerializer(serializers.ModelSerializer):
    subjects = repo_serializers.SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = inspections_models.Expertise
        fields = [
            "digital_resource",
            "date",
            "subjects",
            "direction",
            "digital_complex",
            "expert",
            "date_end",
            "file",
            "remarks",
            "status",
        ]


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = inspections_models.CheckList
        fields = [
            "expertise",
            "type",
            "expert",
            "date",
            "protocol",
        ]


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = inspections_models.Question
        fields = [
            "title",
            "checklist",
            "answer",
        ]
