from . import models

from rest_framework import serializers


class DigitalResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DigitalResource
        fields = (
            'pk', 
            'title', 
            'type', 
            'description', 
            'created', 
            'last_updated', 
            'keywords', 
            'format', 
            'content_count', 
            'usage_stats', 
            'programs_count', 
        )


class DirectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Direction
        fields = (
            'pk', 
            'id', 
            'title', 
            'created', 
            'last_updated', 
        )


class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Language
        fields = (
            'pk', 
            'code', 
            'title', 
            'created', 
            'last_updated', 
        )


class CompetenceCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.CompetenceCategory
        fields = (
            'pk', 
            'id', 
            'title', 
            'created', 
            'last_updated', 
        )


class CompetenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Competence
        fields = (
            'pk', 
            'id', 
            'code', 
            'created', 
            'last_updated', 
            'title', 
        )


class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Platform
        fields = (
            'pk', 
            'title', 
            'logo', 
            'created', 
            'last_updated', 
            'url', 
            'description', 
            'contacts', 
        )


class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Organisation
        fields = (
            'pk', 
            'title', 
            'description', 
            'created', 
            'last_updated', 
            'logo', 
            'site_url', 
            'contacts', 
        )


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Author
        fields = (
            'pk', 
            'title', 
            'description', 
            'created', 
            'last_updated', 
            'image', 
        )


class SourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Source
        fields = (
            'pk', 
            'link', 
            'status', 
            'created', 
            'last_updated', 
            'type', 
            'file', 
            'priority', 
        )


class ResourceStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResourceStatus
        fields = (
            'pk', 
            'status', 
            'model', 
            'created', 
            'last_updated', 
            'due_date', 
        )


class DisciplineThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DisciplineTheme
        fields = (
            'pk', 
            'index', 
            'title', 
            'created', 
            'last_updated', 
        )


class DisciplineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Discipline
        fields = (
            'pk', 
            'title', 
            'description', 
            'created', 
            'last_updated', 
            'labor', 
        )


class ThematicPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ThematicPlan
        fields = (
            'pk', 
            'created', 
            'last_updated', 
        )


class DisciplineThemeResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DisciplineThemeResource
        fields = (
            'pk', 
            'created', 
            'last_updated', 
        )


