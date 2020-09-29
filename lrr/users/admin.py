from django import forms as form
from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

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


class PersonAdmin(admin.ModelAdmin):
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


class StudentAdmin(admin.ModelAdmin):
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


class AcademicGroupAdmin(admin.ModelAdmin):
    form = AcademicGroupAdminForm
    list_display = [
        "number",
    ]


admin.site.register(models.AcademicGroup, AcademicGroupAdmin)
admin.site.register(models.Student, StudentAdmin)
admin.site.register(models.Person, PersonAdmin)
