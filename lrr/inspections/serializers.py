# -*- coding: utf-8 -*-
import logging

from rest_framework import serializers

from lrr.inspections import models as inspections_models
from lrr.repository import serializers as repo_serializers

logger = logging.getLogger(__name__)


class RequestSerializer(serializers.ModelSerializer):
    subjects = repo_serializers.SubjectSerializer(many=True, read_only=True)

    class Meta:
        model = inspections_models.ExpertiseRequest
        fields = [
            "digital_resource",
            "date",
            "subjects",
            "directions",
            "digital_complexes",
            "expert",
            "date_end",
            "file",
            "remarks",
            "status",
        ]


class RequestSubjectListSerializer(serializers.ModelSerializer):
    # subjects = repo_serializers.SubjectSerializer(many=True, read_only=True)
    pk = serializers.CharField(source='digital_resource.pk')
    title = serializers.CharField(source='digital_resource.title')
    platform = serializers.CharField(source='digital_resource.platform')
    type = serializers.CharField(source='digital_resource.get_type_display')
    copyright_holder = serializers.CharField(source='digital_resource.copyright_holder')

    class Meta:
        model = inspections_models.ExpertiseRequest
        fields = [
            "pk",
            "title",
            "platform",
            "type",
            "copyright_holder",
        ]


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = inspections_models.ExpertiseOpinion
        fields = [
            "expertise_request",
            "type",
            "expert",
            "date",
            "protocol",
        ]
