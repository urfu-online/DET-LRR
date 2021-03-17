from allauth.account.forms import SignupForm
from django import forms as form
from django.contrib.auth import forms, get_user_model
from django_select2 import forms as s2forms

from lrr.users import models

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = models.Person


class UserSignupForm(SignupForm):
    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(UserSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user


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


class PersonWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "first_name__icontains",
        "middle_name__icontains",
        "last_name__icontains",
    ]
    max_results = 50


class ExpertForm(form.ModelForm):
    class Meta:
        model = models.Expert
        fields = [
            "person",
            "type",
            "subdivision",
        ]
        widgets = {
            "person": form.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "type": form.Select(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
            "subdivision": form.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': 'false',
                },
            ),
        }

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
