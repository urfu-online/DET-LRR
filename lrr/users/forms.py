from django import forms as form
from django.contrib.auth import forms, get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from lrr.users import models

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = models.Person


class UserCreationForm(forms.UserCreationForm):
    error_message = forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class StudentForm(form.ModelForm):
    class Meta:
        model = models.Student
        fields = [
            "academic_group",
            "person",
        ]


class PersonForm(form.ModelForm):
    class Meta:
        model = models.Person
        fields = [
            "location",
            "date_birthday",
            "city",
            "middle_name",
            "country",
            "first_name",
            "avatar",
            "last_name",
            "user",
        ]


# class SignupForm(form.Form):
#     class Meta:
#         model = models.Person
#         fields = [
#             "middle_name",
#             "first_name",
#             "last_name",
#             "user",
#         ]
#
#     first_name = form.CharField(max_length=100, label='Имя')
#     last_name = form.CharField(max_length=100, label='Фамилия')
#     middle_name = form.CharField(max_length=100, label='Отчество')
#
#     def signup(self, request, user):
#         user.person.first_name = self.cleaned_data['first_name']
#         user.person.last_name = self.cleaned_data['last_name']
#         user.person.middle_name = self.cleaned_data['middle_name']
#         user.person.save()
