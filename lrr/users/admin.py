from django import forms as form
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from import_export.admin import ImportExportModelAdmin

from lrr.users import models
from lrr.users.forms import UserChangeForm, UserSignupForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserSignupForm
    fieldsets = (("User", {"fields": ("name",)}),) + auth_admin.UserAdmin.fieldsets
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(models.Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = [
        "last_name",
        "first_name",
        "middle_name",
        "location",
        "date_birthday",
        "city",
        "country",

    ]
    readonly_fields = [
        "created",
    ]
    search_fields = ["last_name", "user__email", "user__username", "first_name", "middle_name", ]


@admin.register(models.Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = [
        "person",
        "academic_group",
    ]
    readonly_fields = [
        "created",
    ]


class AcademicGroupAdminForm(form.ModelForm):
    class Meta:
        model = models.AcademicGroup
        fields = "__all__"


@admin.register(models.AcademicGroup)
class AcademicGroupAdmin(ImportExportModelAdmin):
    form = AcademicGroupAdminForm
    list_display = [
        "number",
    ]
    search_fields = ['number']


@admin.register(models.Expert)
class ExpertAdmin(ImportExportModelAdmin):
    list_display = [
        "person",
        "subdivision",
    ]
    filter_horizontal = ('types',)
    search_fields = ['person__user__email', 'person__last_name']


@admin.register(models.ChoicesExpert)
class ChoicesExpertAdmin(admin.ModelAdmin):
    list_display = [
        "type"
    ]


@admin.register(models.GroupDisciplines)
class GroupDisciplinesAdmin(ImportExportModelAdmin):
    list_display = [
        "academic_group",
        "subject",
        "semestr",
    ]
    exclude = ["id", "created", "last_updated"]
    search_fields = ["academic_group", "subject", "semestr"]
