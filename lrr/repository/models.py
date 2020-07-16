# -*- coding: utf-8 -*-
import uuid

from django.conf import settings
from django.db import models as models
from django.urls import reverse

from datetime import datetime


def get_source_path(instance, filename):
    return f"{datetime.now().year}res_id_{instance.id}/{filename}"


class DigitalResource(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField("Наименование", max_length=1024)
    type = models.TextField("Тип", max_length=100)
    description = models.TextField("Описание", )
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)
    keywords = models.CharField("Ключевые слова", max_length=150)
    format = models.CharField(max_length=30)
    content_count = models.PositiveIntegerField("Показатель объема контента")
    usage_stats = models.PositiveIntegerField("Показатель использования")
    programs_count = models.PositiveIntegerField("Показатель назначения")

    # Relationship Fields
    directions = models.ManyToManyField(
        'repository.Direction',
        related_name="digitalresources",
    )
    disciplines = models.ManyToManyField(
        'repository.Discipline',
        related_name="digitalresources",
    )
    language = models.ForeignKey(
        'repository.Language',
        on_delete=models.CASCADE, related_name="digitalresources",
    )
    rightholder = models.ForeignKey(
        'repository.Organisation',
        on_delete=models.CASCADE, related_name="digitalresources",
    )
    competences = models.ManyToManyField(
        'repository.Competence',
        related_name="digitalresources",
    )
    platform = models.ForeignKey(
        'repository.Platform',
        on_delete=models.CASCADE, related_name="digitalresources",
    )
    authors = models.ManyToManyField(
        'repository.Author',
        related_name="digitalresources",
    )
    sources = models.ManyToManyField(
        'repository.Source',
        related_name="digitalresources",
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="digitalresources",
    )
    status = models.OneToOneField(
        'repository.ResourceStatus',
        on_delete=models.CASCADE, related_name="digitalresources",
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_digitalresource_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_digitalresource_update', args=(self.pk,))


class Direction(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Наименование", max_length=255, editable=True)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_direction_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_direction_update', args=(self.pk,))


class Language(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField("Код языка", max_length=4)
    title = models.CharField("Наименование", max_length=100)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_language_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_language_update', args=(self.pk,))


class CompetenceCategory(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Наименование", max_length=100)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_competencecategory_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_competencecategory_update', args=(self.pk,))


class Competence(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField("Код компетенции", max_length=30)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)
    title = models.CharField("Наименование", max_length=150)

    # Relationship Fields
    category = models.ForeignKey(
        'repository.CompetenceCategory', related_name="competences", on_delete=models.PROTECT
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_competence_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_competence_update', args=(self.pk,))


class Platform(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Наименование", max_length=150)
    logo = models.ImageField("Логотип", upload_to="images/platforms/logo/")
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)
    url = models.URLField("URL", max_length=255)
    description = models.TextField("Описание", max_length=1024)
    contacts = models.TextField("Контакты", max_length=1024)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_platform_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_platform_update', args=(self.pk,))


class Organisation(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Наименование", max_length=150)
    description = models.TextField("Описание", max_length=1024)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)
    logo = models.ImageField("Логотип", upload_to="images/org/logo/")
    site_url = models.URLField("URL сайта", max_length=255)
    contacts = models.TextField("Контакты", max_length=1024)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_organisation_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_organisation_update', args=(self.pk,))


class Author(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Наименование", max_length=255)
    description = models.TextField("Описание", max_length=1024)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)
    image = models.ImageField("Фото", upload_to='images/author/photos/')

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_author_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_author_update', args=(self.pk,))


class Source(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.URLField("Ссылка", max_length=255)
    status = models.CharField("Статус", max_length=255)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)
    type = models.CharField("Тип", max_length=255)
    file = models.FileField("Файл", upload_to=get_source_path)
    priority = models.PositiveIntegerField("Приоритет")

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_source_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_source_update', args=(self.pk,))


class ResourceStatus(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField("Статус", max_length=150)
    model = models.CharField("Модель использования", max_length=255)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)
    due_date = models.CharField("Статус", max_length=255)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_resourcestatus_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_resourcestatus_update', args=(self.pk,))


class DisciplineTheme(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    index = models.CharField("Индекс", max_length=255)
    title = models.CharField("Наименование", max_length=255)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def discipline(self):
        return self.thematicplan_set.first().discipline

    def get_absolute_url(self):
        return reverse('repository:repository_disciplinetheme_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_disciplinetheme_update', args=(self.pk,))


class Discipline(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Наименование", max_length=255)
    description = models.CharField("Описание", max_length=1024)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)
    labor = models.PositiveSmallIntegerField("Трудоемкость")

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_discipline_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_discipline_update', args=(self.pk,))


class ThematicPlan(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)

    # Relationship Fields
    discipline = models.ForeignKey(
        'repository.Discipline', related_name="thematicplans", on_delete=models.PROTECT
    )
    themes = models.ManyToManyField(
        'repository.DisciplineTheme'
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_thematicplan_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_thematicplan_update', args=(self.pk,))


class DisciplineThemeResource(models.Model):
    # Fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последнее обновление", auto_now=True, editable=False)

    # Relationship Fields
    digital_resource_source = models.ForeignKey(
        'repository.Source',
        on_delete=models.CASCADE, related_name="disciplinethemeresources",
    )
    discipline_themes = models.ForeignKey(
        'repository.DisciplineTheme',
        on_delete=models.CASCADE, related_name="disciplinethemeresources",
    )

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('repository:repository_disciplinethemeresource_detail', args=(self.pk,))

    def get_update_url(self):
        return reverse('repository:repository_disciplinethemeresource_update', args=(self.pk,))
