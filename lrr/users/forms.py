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
