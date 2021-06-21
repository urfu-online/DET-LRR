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


class PersonAdminForm(form.ModelForm):
    class Meta:
        model = models.Person
        fields = "__all__"


class PersonAdmin(ImportExportModelAdmin):
    form = PersonAdminForm
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


class StudentAdminForm(form.ModelForm):
    class Meta:
        model = models.Student
        fields = "__all__"


class StudentAdmin(ImportExportModelAdmin):
    form = StudentAdminForm
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


class AcademicGroupAdmin(ImportExportModelAdmin):
    form = AcademicGroupAdminForm
    list_display = [
        "number",
    ]
    search_fields = ['number']


class ExpertAdminForm(form.ModelForm):
    class Meta:
        model = models.Expert
        fields = "__all__"


class ChoicesExpertAdminForm(form.ModelForm):
    class Meta:
        model = models.ChoicesExpert
        fields = "__all__"


class ExpertAdmin(ImportExportModelAdmin):
    form = ExpertAdminForm
    list_display = [
        "person",
        "subdivision",
    ]
    filter_horizontal = ('types',)


class ChoicesExpertAdmin(admin.ModelAdmin):
    form = ChoicesExpertAdminForm
    list_display = [
        "type"
    ]


class GroupDisciplinesAdminForm(form.ModelForm):
    class Meta:
        model = models.GroupDisciplines
        fields = "__all__"


class GroupDisciplinesAdmin(ImportExportModelAdmin):
    form = GroupDisciplinesAdminForm
    list_display = [
        "academic_group",
        "subject",
        "semestr",
    ]
    exclude = ["id", "created", "last_updated"]


admin.site.register(models.GroupDisciplines, GroupDisciplinesAdmin)
admin.site.register(models.ChoicesExpert, ChoicesExpertAdmin)
admin.site.register(models.Expert, ExpertAdmin)
admin.site.register(models.AcademicGroup, AcademicGroupAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Person, PersonAdmin)
