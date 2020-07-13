from django.contrib import admin
from django import forms
from .models import DigitalResource, Direction, Language, CompetenceCategory, Competence, Platform, Organisation, \
    Author, Source, ResourceStatus, DisciplineTheme, Discipline, ThematicPlan, DisciplineThemeResource


class DigitalResourceAdminForm(forms.ModelForm):
    class Meta:
        model = DigitalResource
        fields = '__all__'


class DigitalResourceAdmin(admin.ModelAdmin):
    form = DigitalResourceAdminForm
    list_display = ['title', 'type', 'description', 'created', 'last_updated', 'keywords', 'format', 'content_count',
                    'usage_stats', 'programs_count']
    readonly_fields = ['id', 'content_count', 'usage_stats', 'programs_count']


admin.site.register(DigitalResource, DigitalResourceAdmin)


class DirectionAdminForm(forms.ModelForm):
    class Meta:
        model = Direction
        fields = '__all__'


class DirectionAdmin(admin.ModelAdmin):
    form = DirectionAdminForm
    list_display = ['id', 'title', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(Direction, DirectionAdmin)


class LanguageAdminForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'


class LanguageAdmin(admin.ModelAdmin):
    form = LanguageAdminForm
    list_display = ['code', 'title', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(Language, LanguageAdmin)


class CompetenceCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = CompetenceCategory
        fields = '__all__'


class CompetenceCategoryAdmin(admin.ModelAdmin):
    form = CompetenceCategoryAdminForm
    list_display = ['id', 'title', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(CompetenceCategory, CompetenceCategoryAdmin)


class CompetenceAdminForm(forms.ModelForm):
    class Meta:
        model = Competence
        fields = '__all__'


class CompetenceAdmin(admin.ModelAdmin):
    form = CompetenceAdminForm
    list_display = ['id', 'code', 'created', 'last_updated', 'title']
    readonly_fields = ['id', 'code', 'title', 'created', 'last_updated']


admin.site.register(Competence, CompetenceAdmin)


class PlatformAdminForm(forms.ModelForm):
    class Meta:
        model = Platform
        fields = '__all__'


class PlatformAdmin(admin.ModelAdmin):
    form = PlatformAdminForm
    list_display = ['title', 'logo', 'url', 'description', 'contacts', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(Platform, PlatformAdmin)


class OrganisationAdminForm(forms.ModelForm):
    class Meta:
        model = Organisation
        fields = '__all__'


class OrganisationAdmin(admin.ModelAdmin):
    form = OrganisationAdminForm
    list_display = ['title', 'description', 'logo', 'site_url', 'contacts', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(Organisation, OrganisationAdmin)


class AuthorAdminForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorAdmin(admin.ModelAdmin):
    form = AuthorAdminForm
    list_display = ['title', 'description', 'image', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(Author, AuthorAdmin)


class SourceAdminForm(forms.ModelForm):
    class Meta:
        model = Source
        fields = '__all__'


class SourceAdmin(admin.ModelAdmin):
    form = SourceAdminForm
    list_display = ['link', 'status', 'type', 'file', 'priority', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(Source, SourceAdmin)


class ResourceStatusAdminForm(forms.ModelForm):
    class Meta:
        model = ResourceStatus
        fields = '__all__'


class ResourceStatusAdmin(admin.ModelAdmin):
    form = ResourceStatusAdminForm
    list_display = ['status', 'model', 'due_date', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(ResourceStatus, ResourceStatusAdmin)


class DisciplineThemeAdminForm(forms.ModelForm):
    class Meta:
        model = DisciplineTheme
        fields = '__all__'


class DisciplineThemeAdmin(admin.ModelAdmin):
    form = DisciplineThemeAdminForm
    list_display = ['index', 'title', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(DisciplineTheme, DisciplineThemeAdmin)


class DisciplineAdminForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = '__all__'


class DisciplineAdmin(admin.ModelAdmin):
    form = DisciplineAdminForm
    list_display = ['title', 'description', 'labor', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(Discipline, DisciplineAdmin)


class ThematicPlanAdminForm(forms.ModelForm):
    class Meta:
        model = ThematicPlan
        fields = '__all__'


class ThematicPlanAdmin(admin.ModelAdmin):
    form = ThematicPlanAdminForm
    list_display = ['id', 'created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(ThematicPlan, ThematicPlanAdmin)


class DisciplineThemeResourceAdminForm(forms.ModelForm):
    class Meta:
        model = DisciplineThemeResource
        fields = '__all__'


class DisciplineThemeResourceAdmin(admin.ModelAdmin):
    form = DisciplineThemeResourceAdminForm
    list_display = ['created', 'last_updated']
    readonly_fields = ['id', 'created', 'last_updated']


admin.site.register(DisciplineThemeResource, DisciplineThemeResourceAdmin)
