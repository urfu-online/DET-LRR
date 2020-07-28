from rest_framework import serializers

from . import models


class StatusCORSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.StatusCOR
        fields = [
            "created",
            "quality_category",
            "interactive_category",
        ]

class ExpertiseStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ExpertiseStatus
        fields = [
            "last_updated",
            "end_date",
            "status",
            "accepted_status",
            "created",
        ]

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Subject
        fields = [
            "description",
            "created",
            "title",
            "last_updated",
            "labor",
        ]

class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Organization
        fields = [
            "last_updated",
            "description",
            "logo",
            "contacts",
            "title",
            "created",
            "url",
        ]


class EduProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EduProgram
        fields = [
            "description",
            "last_updated",
            "created",
            "short_description",
            "title",
        ]

class ProvidingDisciplineSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ProvidingDiscipline
        fields = [
            "rate",
            "created",
            "last_updated",
        ]

class ResultEduSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResultEdu
        fields = [
            "title",
            "last_updated",
            "created",
            "description",
        ]

class DigitalResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.DigitalResource
        fields = [
            "id",
            "title",
            "created",
            "type",
            "source_data",
            "last_updated",
            "ketwords",
            "description",
        ]

class CompetenceSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Competence
        fields = [
            "created",
            "title",
            "code",
        ]

class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Platform
        fields = [
            "created",
            "url",
            "logo",
            "description",
            "contacts",
            "title",
        ]

class LanguageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Language
        fields = [
            "code",
            "titile",
            "created",
        ]

class SubjectTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SubjectTag
        fields = [
            "created",
            "last_updated",
        ]

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Student
        fields = [
            "academic_group",
            "created",
        ]

class ConformityThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ConformityTheme
        fields = [
            "practice",
            "theory",
            "created",
            "last_updated",
        ]

class EduProgramTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EduProgramTag
        fields = [
            "created",
            "last_updated",
        ]

class SubjectThemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SubjectTheme
        fields = [
            "description",
            "created",
            "title",
        ]

class ThematicPlanSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ThematicPlan
        fields = [
            "created",
            "title",
        ]

class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Person
        fields = [
            "location",
            "date_birthday",
            "city",
            "created",
            "middle_name",
            "country",
            "first_name",
            "avatar",
            "last_name",
        ]
