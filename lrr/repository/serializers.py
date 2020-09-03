import logging

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
            "expertise_status",
            "quality_category",
            "interactive_category",
        ]


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = [
            "id",
            "title",
            "description",
            "contacts",
            "url",
            "url_logo"
        ]


class EduProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EduProgram
        fields = [
            "title",
            "description",
            "short_description",
        ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = [
            "title",
            "description",
            "labor"
        ]


class SubjectTagSerializer(serializers.ModelSerializer):
    tag = SubjectSerializer(many=False, read_only=True)

    class Meta:
        model = models.SubjectTag
        fields = [
            "id",
            "tag",
        ]


class EduProgramTagSerializer(serializers.ModelSerializer):
    tag = EduProgramSerializer(many=False, read_only=True)

    class Meta:
        model = models.EduProgramTag
        fields = [
            "id",
            "tag"
        ]


class ExpertiseStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ExpertiseStatus
        fields = [
            "id",
            "end_date",
            "status",
            "accepted_status",
        ]


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = [
            "id",
            "title",
            "description",
            "labor",
        ]


class ProvidingDisciplineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProvidingDiscipline
        fields = [
            "id",
            "rate",
        ]


class ResultEduSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResultEdu
        fields = [
            "title",
            "description",
            "competence"
        ]


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Language
        fields = [
            "code",
            "title",
        ]


# class DigitalResourceCompetenceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.DigitalResourceCompetence
#         fields = [
#             "digital_resource",
#             "competence"
#         ]


class DigitalResourceSerializer(serializers.ModelSerializer):
    authors = PersonSerializer(many=True, read_only=False)
    # owner = PersonSerializer(many=False, read_only=False)
    subjects_tags = SubjectTagSerializer(many=True, read_only=False)
    edu_programs_tags = EduProgramTagSerializer(many=True, read_only=False)
    result_edu = ResultEduSerializer(many=True, read_only=False)

    class Meta:
        model = models.DigitalResource
        fields = [
            "id",
            "title",
            "type",
            "source_data",
            "description",
            "language",
            "keywords",
            "platform",
            "copyright_holder",
            "authors",
            "subjects_tags",
            "edu_programs_tags",
            # "owner",
            "result_edu",

            "last_updated",
            "created",
        ]

    def create(self, validated_data):
        # Ищем, если не нашли, то создаем зависимые объекты
        logger.warning(validated_data)
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

        results_edu_data = validated_data.pop('result_edu')
        results_edu = []
        for result_edu_data in results_edu_data:
            results_edu.append(models.ResultEdu.objects.create(**result_edu_data))

        # Создаем объект DR
        dr = models.DigitalResource.objects.create(**validated_data)
        dr.authors.set(authors)
        dr.subjects_tags.set(subjects_tags)
        dr.edu_programs_tags.set(edu_programs_tags)
        dr.result_edu.set(results_edu)
        return dr


class CompetenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Competence
        fields = [
            "id",
            "title",
            "code",
        ]


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Platform
        fields = [
            "id",
            "title",
            "url",
            "url_logo",
            "description",
            "contacts",
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
        ]


class SubjectThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubjectTheme
        fields = [
            "id",
            "title",
            "description",
        ]


class ThematicPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ThematicPlan
        fields = [
            "id",
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
#    "keywords":null,
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
