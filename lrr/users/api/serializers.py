from django.contrib.auth import get_user_model
from rest_framework import serializers

from lrr.users import models

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = [
            "academic_group",
            "created",
        ]


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Person
        fields = [
            "first_name",
            "middle_name",
            "last_name",
            "location",
            "date_birthday",
            "city",
            "country",
        ]
