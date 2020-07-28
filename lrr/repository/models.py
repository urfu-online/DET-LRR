# -*- coding: utf-8 -*-
import uuid

from django.conf import settings
from django.db import models as models
from django.urls import reverse

from datetime import datetime


class StatusCOR(models.Model):
    # quality_category
    INNER = '0'
    OUTER = '1'
    OUTSIDE = '2'

    QUALITY_CATEGORIES = [
        (INNER, 'внутренний'),
        (OUTER, 'внешний'),
        (OUTSIDE, 'сторонний'),
    ]

    # interactive_category
    NOT_INTERACTIVE = '0'
    WITH_TEACHER_SUPPORT = '1'
    AUTO = '2'

    INTERACTIVE_CATEGORIES = [
        (NOT_INTERACTIVE, 'не интерактивный'),
        (WITH_TEACHER_SUPPORT, 'с поддержкой преподавателя'),
        (AUTO, 'автоматизированный'),
    ]

    # Relationships
    expertise_status = models.ForeignKey("repository.ExpertiseStatus", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    quality_category = models.CharField(max_length=30, choices=QUALITY_CATEGORIES, blank=True)
    interactive_category = models.CharField(max_length=30, choices=INTERACTIVE_CATEGORIES, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Status_COR_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Status_COR_update", args=(self.pk,))


class ExpertiseStatus(models.Model):
    # status
    NO_INIT = '0'
    SUB_APP = '1'
    ON_EXPERTISE = '2'
    ON_REVISION = '3'
    ASSIGNED_STATUS = '4'

    STATUS_CHOICES = [
        (NO_INIT, 'не инициирована'),
        (SUB_APP, 'подана заявка'),
        (ON_EXPERTISE, 'на экспертизе'),
        (ON_REVISION, 'на доработку'),
        (ASSIGNED_STATUS, 'присвоен статус'),
    ]

    # Fields
    last_updated = models.DateTimeField("Последние обнолвение", auto_now=True, editable=False)
    end_date = models.DateTimeField("Срок действия")
    status = models.CharField("Состояние экспертизы", max_length=30, choices=STATUS_CHOICES, default=NO_INIT)
    accepted_status = models.BooleanField("Утверждено (присвоен статус)", default=False)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Expertise_status_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Expertise_status_update", args=(self.pk,))


class Subject(models.Model):
    # Fields
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    title = models.CharField("Наименование", max_length=100)
    last_updated = models.DateTimeField("Последние обнолвение", auto_now=True, editable=False)
    labor = models.PositiveSmallIntegerField("Трудоемкость", null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Subject_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Subject_update", args=(self.pk,))


class Organization(models.Model):
    # Fields
    last_updated = models.DateTimeField("Последние обнолвение", auto_now=True, editable=False)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    logo = models.ImageField("Логотип", upload_to="upload/images/", null=True, blank=True)
    contacts = models.TextField("Контакты", max_length=500, null=True, blank=True)
    title = models.CharField("Наименование", max_length=150)
    created = models.DateTimeField("Созданно", auto_now_add=True, editable=False)
    url = models.URLField("URL", null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Organization_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Organization_update", args=(self.pk,))


class EduProgram(models.Model):
    # Fields
    description = models.TextField("Описание", max_length=1024, null=True, blank=True)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)
    created = models.DateTimeField("Созданно", auto_now_add=True, editable=False)
    short_description = models.CharField("Короткое описание", max_length=300, null=True, blank=True)
    title = models.CharField("Наименование", max_length=150)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_EduProgram_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_EduProgram_update", args=(self.pk,))


class ProvidingDiscipline(models.Model):
    # Relationships
    edu_program = models.ForeignKey("repository.EduProgram", on_delete=models.PROTECT)
    subject = models.ForeignKey("repository.Subject", on_delete=models.PROTECT)

    # Fields
    rate = models.PositiveIntegerField("Процент покрытия")
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Providing_discipline_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Providing_discipline_update", args=(self.pk,))


class ResultEdu(models.Model):
    # Fields
    title = models.CharField("Наименование", max_length=150)
    digital_resource_competence = models.ForeignKey("repository.DigitalResourceCompetence", on_delete=models.CASCADE)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)
    created = models.DateTimeField("Созданно", auto_now_add=True, editable=False)
    description = models.TextField("Описание", max_length=500)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_ResultEdu_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_ResultEdu_update", args=(self.pk,))


class DigitalResource(models.Model):
    # source_data
    NULL = '0'
    MANUAL = '1'
    IMPORT = '2'

    SOURCES = [
        (NULL, ''),
        (MANUAL, 'вручную'),
        (IMPORT, 'импорт'),
    ]

    # type
    OK = '0'
    EUK = '1'
    TEXT_EOR = '2'
    MULTIMEDIA_EOR = '3'

    RESOURCE_TYPE = [
        (OK, 'Онлайн-курс'),
        (EUK, 'ЭУК'),  # что такое ЭУК ?
        (TEXT_EOR, 'Текстовый электронный образовательный ресурс'),
        (MULTIMEDIA_EOR, 'Мультимедийный электронный образовательный ресурс'),
    ]

    # Relationships
    edu_programs_tags = models.ManyToManyField("EduProgramTag")
    authors = models.ManyToManyField("Person", verbose_name="Авторы", blank=True,
                                     related_name="authors_digital_resource")
    copyright_holder = models.ForeignKey("Organization", on_delete=models.PROTECT)
    subjects_tags = models.ManyToManyField("SubjectTag")
    status_cor = models.ForeignKey("StatusCOR", on_delete=models.CASCADE)
    owner = models.ForeignKey("Person", on_delete=models.PROTECT, related_name="owner_digital_resource")
    language = models.ForeignKey("Language", on_delete=models.PROTECT)
    provided_disciplines = models.ManyToManyField("ProvidingDiscipline")
    platform = models.ForeignKey("Platform", on_delete=models.PROTECT)

    # Fields
    id = models.UUIDField("ID ресурса", primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Наименование", max_length=150)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    type = models.CharField("Тип ресурса", max_length=30, choices=RESOURCE_TYPE, null=True)
    source_data = models.CharField("Источник данных", max_length=30, choices=SOURCES, null=True,
                                   default=NULL)  # TODO исправить НУЛЛ на проде
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)
    ketwords = models.CharField("Ключевые слова", max_length=100, null=True, blank=True)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_DigitalResource_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_DigitalResource_update", args=(self.pk,))


class DigitalResourceCompetence(models.Model):
    digital_resource = models.ForeignKey("repository.DigitalResource", on_delete=models.CASCADE)
    competence = models.ForeignKey("repository.Competence", on_delete=models.PROTECT)

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_DigitalResourceCompetence_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_DigitalResourceCompetence_update", args=(self.pk,))


class Competence(models.Model):
    # Fields
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    title = models.CharField("Наименование", max_length=150)
    code = models.CharField("Код компетенции", max_length=8)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Competence_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Competence_update", args=(self.pk,))


class Platform(models.Model):
    # Fields
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    url = models.URLField("Ссылка")
    logo = models.ImageField("Логотп", upload_to="upload/images/", null=True, blank=True)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    contacts = models.TextField("Контакты", max_length=500, null=True, blank=True)
    title = models.CharField("Наимаенование", max_length=150)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Platform_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Platform_update", args=(self.pk,))


class Language(models.Model):
    # Fields
    code = models.CharField("Код языка", max_length=4)
    titile = models.CharField("Наименование", max_length=80)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Language_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Language_update", args=(self.pk,))


class SubjectTag(models.Model):
    # Relationships
    tag = models.ForeignKey("repository.Subject", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_SubjectTag_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_SubjectTag_update", args=(self.pk,))


class Student(models.Model):
    # Relationships
    person = models.ForeignKey("repository.Person", on_delete=models.CASCADE)

    # Fields
    academic_group = models.CharField("Академическая группа", max_length=30)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Student_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Student_update", args=(self.pk,))


class ConformityTheme(models.Model):
    # Relationships
    theme = models.ForeignKey("repository.SubjectTheme", on_delete=models.CASCADE)
    providing_discipline = models.ForeignKey("repository.ProvidingDiscipline", on_delete=models.CASCADE)

    # Fields
    practice = models.NullBooleanField("Практика")
    theory = models.NullBooleanField("Теория")
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_ConformityTheme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_ConformityTheme_update", args=(self.pk,))


class EduProgramTag(models.Model):
    # Relationships
    tag = models.ForeignKey("repository.EduProgram", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_EduProgramTag_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_EduProgramTag_update", args=(self.pk,))


class SubjectTheme(models.Model):
    # Fields
    thematic_plan = models.ForeignKey("repository.ThematicPlan", on_delete=models.PROTECT)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    title = models.CharField("Наимаенование", max_length=150)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_SubjectTheme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_SubjectTheme_update", args=(self.pk,))


class ThematicPlan(models.Model):
    # Relationships
    subject = models.ForeignKey("repository.Subject", on_delete=models.PROTECT)
    edu_programs = models.ForeignKey("repository.EduProgram", on_delete=models.PROTECT)

    # Fields
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    title = models.CharField("Наименование", max_length=50)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_ThematicPlan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_ThematicPlan_update", args=(self.pk,))


class Person(models.Model):
    # Relationships
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    # Fields
    location = models.CharField("Адрес проживания", max_length=150, null=True, blank=True)
    date_birthday = models.DateTimeField("Дата рождения", null=True, blank=True)
    city = models.CharField("Город", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    middle_name = models.CharField("Фамилия", max_length=100)
    country = models.CharField("Страна", max_length=100, null=True, blank=True)
    first_name = models.CharField("Имя", max_length=45)
    avatar = models.ImageField("Изображение профиля", upload_to="upload/images/", null=True, blank=True)
    last_name = models.CharField("Отчество", max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Person_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Person_update", args=(self.pk,))
