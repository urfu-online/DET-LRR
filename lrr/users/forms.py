from allauth.account.forms import SignupForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, HTML, Field
from django import forms as form
from django.conf import settings
from django.contrib.auth import forms, get_user_model
from django.forms import DateField, TextInput
from django_select2 import forms as s2forms

from lrr.users import models

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = models.Person


class UserSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(UserSignupForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.use_custom_control = True
        self.helper.render_hidden_fields = False

        for field in self._meta.fields:
            self.fields[field].help_text = self.fields[field].label
            self.fields[field].label = ""

        self.helper.layout = Layout(
            Field('email', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('username', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('password1', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('password2', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
        )

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(UserSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user

    class Meta:
        model = User
        fields = [
            "email",
            "username",
            "password1",
            "password2",
        ]


class StudentForm(form.ModelForm):
    class Meta:
        model = models.Student
        fields = [
            "academic_group",
            "person",
        ]


class PersonForm(form.ModelForm):
    date_birthday = DateField(
        widget=TextInput(
            attrs={'type': 'date'}
        )
    )

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.use_custom_control = True
        self.helper.render_hidden_fields = False
        # ['first_name', 'middle_name', 'last_name', 'location', 'avatar', 'date_birthday']

        for field in self._meta.fields:
            self.fields[field].help_text = self.fields[field].label
            self.fields[field].label = ""

        self.helper.layout = Layout(
            Field('person', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('types', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('subdivision', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
        )

        self.fields['first_name'].help_text = "Имя"
        self.fields['middle_name'].help_text = "Отчество, если есть"
        self.fields['last_name'].help_text = "Фамилия"
        self.fields['avatar'].help_text = "Аватар"
        self.fields['date_birthday'].help_text = "Дата рождения"
        self.fields['city'].help_text = "Город"
        self.helper.layout = Layout(
            Field('first_name', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('middle_name', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('last_name', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            HTML(f"""
            <div class="custom-file mt-4" id="div_id_avatar">
                <input type="file" class="custom-file-input shadow-sm bg-white border border-secondary" id="id_avatar" name="avatar">
                <small id="hint_id_avatar" class="form-text text-muted">Аватар</small>
                <label class="custom-file-label" for="id_avatar"></label>
              </div>
            """),
            Field('date_birthday', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            # Field('location', placeholder="", css_class="mt-4 shadow-sm bg-white border border-secondary address pac-target-input"),

        )

    class Meta:
        model = models.Person
        fields = ["first_name", "middle_name", "last_name", "avatar", "date_birthday", "city", ]


class PersonWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "first_name__icontains",
        "middle_name__icontains",
        "last_name__icontains",
    ]
    max_results = 50


class ExpertWidget(s2forms.ModelSelect2Widget):
    pass


class ExpertForm(form.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ExpertForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.render_hidden_fields = False
        # ['first_name', 'middle_name', 'last_name', 'location', 'avatar', 'date_birthday']

        for field in self._meta.fields:
            self.fields[field].help_text = self.fields[field].label
            self.fields[field].label = ""

        self.helper.layout = Layout(
            Field('person', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('types', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
            Field('subdivision', placeholder="", css_class=settings.DEFAULT_FORMFIELD_CLASSES),
        )

    class Meta:
        model = models.Expert
        fields = [
            "person",
            "types",
            "subdivision",
        ]

        widgets = {
            'types': s2forms.Select2Widget,
            'person': PersonWidget(select2_options={
                'minimumResultsForSearch': 10,
                'closeOnSelect': True,
            })
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
