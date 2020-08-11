import logging
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework import serializers

from lrr.users.models import Person
from . import models

logger = logging.getLogger(__name__)

from lrr.users.api.serializers import PersonSerializer


class DRStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DRStatus
        fields = [
            "id",
            "created",
            "quality_category",
            "interactive_category",
        ]


class SubjectTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubjectTag
        fields = [
            "id",
            "created",
            "last_updated",
        ]


class ExpertiseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpertiseStatus
        fields = [
            "id",
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
            "id",
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
            "id",
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
            "id",
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
            "id",
            "rate",
            "created",
            "last_updated",
        ]


class ResultEduSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResultEdu
        fields = [
            "id",
            "title",
            "last_updated",
            "created",
            "description",
        ]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = [
            "code",
            "title",
            "created",
        ]


class DigitalResourceSerializer(serializers.ModelSerializer):
    authors = PersonSerializer(many=True, read_only=False)
    subjects_tags = SubjectTagSerializer(many=True, read_only=False)

    class Meta:
        model = models.DigitalResource
        fields = [
            "id",
            "title",
            "type",
            "source_data",
            "description",
            "language",
            "language",
            "ketwords",
            "platform",
            "copyright_holder",
            "authors",
            "subjects_tags",
            "edu_programs_tags",
            "status_cor",
            "owner",

            "last_updated",
            "created",
        ]

    def create(self, validated_data):
        # Ищем, если не нашли, то создаем зависимые объекты
        authors_data = validated_data.pop('authors')
        authors = []
        for author_data in authors_data:
            # Сделать поиск по персонам. Не создавать новых, если они есть
            authors.append(Person.objects.create(**author_data))

        # Ищем, если не нашли, то создаем зависимые объекты
        subject_tags_data = validated_data.pop('subjects_tags')
        subjects_tags = []
        for subject_tag in subject_tags_data:
            # Сделать поиск по персонам. Не создавать новых, если они есть
            subjects_tags.append(models.SubjectTag.objects.create(**subject_tag))

        # Ищем, если не нашли, то создаем зависимые объекты
        edu_programs_tags_data = validated_data.pop('edu_programs_tags')
        edu_programs_tags = []
        for edu_programs_tag in edu_programs_tags_data:
            # Сделать поиск по персонам. Не создавать новых, если они есть
            edu_programs_tags.append(models.EduProgramTag.objects.create(**edu_programs_tag))

        # Создаем объект DR
        dr = models.DigitalResource.objects.create(**validated_data)
        dr.authors.set(authors)
        dr.subjects_tags.set(subjects_tags)
        dr.edu_programs_tags.set(edu_programs_tags)
        return dr


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competence
        fields = [
            "id",
            "created",
            "title",
            "code",
        ]


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Platform
        fields = [
            "id",
            "created",
            "url",
            "logo",
            "description",
            "contacts",
            "title",
        ]


# class StudentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Student
#         fields = [
# "id",


#             "academic_group",
#             "created",
#         ]

class ConformityThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConformityTheme
        fields = [
            "id",
            "practice",
            "theory",
            "created",
            "last_updated",
        ]


class EduProgramTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EduProgramTag
        fields = [
            "id",
            "created",
            "last_updated",
        ]


class SubjectThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubjectTheme
        fields = [
            "id",
            "description",
            "created",
            "title",
        ]


class ThematicPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ThematicPlan
        fields = [
            "id",
            "created",
            "title",
        ]

#
# class PersonSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = models.Person
#         fields = [
# "id",
#             "location",
#             "date_birthday",
#             "city",
#             "created",
#             "middle_name",
#             "country",
#             "first_name",
#             "avatar",
#             "last_name",
#         ]


# {
#    "title":"ujssdyj",
#    "type":"1",
#    "source_data":"0",
#    "description":"",
#    "language":"bc56d643-04d7-480c-800c-4c20339429f1",
#    "ketwords":null,
#    "platform":"b373e01c-e82e-44f8-a3cd-2440929c8700",
#    "copyright_holder":"1b0fab87-da04-463a-aac8-4c10f1de392f",
#    "authors":[
#       {
#          "middle_name":"z",
#          "first_name":"z",
#          "last_name":"z"
#       }
#    ],
#    "subjects_tags":[
#
#    ],
#    "edu_programs_tags":[
#
#    ]
# }
