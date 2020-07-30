# -*- coding: utf-8 -*-
import uuid

from django.db import models as models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from lrr.users.models import Person, Student


class DateInfo(models.Model):
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обнолвение", auto_now=True, editable=False)

    class Meta:
        abstract = True


class DRStatus(DateInfo):
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
    expertise_status = models.ForeignKey("repository.ExpertiseStatus", verbose_name="Статус экспертизы",
                                         on_delete=models.CASCADE)

    # Fields
    quality_category = models.CharField("Категория качества", max_length=30, choices=QUALITY_CATEGORIES, blank=True)
    interactive_category = models.CharField("Категория интерактивности", max_length=30, choices=INTERACTIVE_CATEGORIES,
                                            blank=True)

    class Meta:
        verbose_name = u"Статус ЦОР"
        verbose_name_plural = u"Статусы ЦОР"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Status_COR_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Status_COR_update", args=(self.pk,))


class ExpertiseStatus(DateInfo):
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

    end_date = models.DateTimeField("Срок действия")
    status = models.CharField("Состояние экспертизы", max_length=30, choices=STATUS_CHOICES, default=NO_INIT)
    accepted_status = models.BooleanField("Утверждено (присвоен статус)", default=False)

    class Meta:
        verbose_name = u"Статус экспертизы"
        verbose_name_plural = u"Статусы экспертиз"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Expertise_status_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Expertise_status_update", args=(self.pk,))


class Subject(DateInfo):
    # Fields
    title = models.CharField("Наименование", max_length=100)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    labor = models.PositiveSmallIntegerField("Трудоемкость", null=True, blank=True)

    class Meta:
        verbose_name = u"Дисциплина"
        verbose_name_plural = u"Дисциплины"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Subject_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Subject_update", args=(self.pk,))


class Organization(DateInfo):
    # Fields
    title = models.CharField("Наименование", max_length=150)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    logo = models.ImageField("Логотип", upload_to="upload/images/", null=True, blank=True)
    contacts = models.TextField("Контакты", max_length=500, null=True, blank=True)
    url = models.URLField("URL", null=True, blank=True)

    class Meta:
        verbose_name = u"Организация"
        verbose_name_plural = u"Организации"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Organization_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Organization_update", args=(self.pk,))


class EduProgram(DateInfo):
    # Fields
    title = models.CharField("Наименование", max_length=150)
    short_description = models.CharField("Короткое описание", max_length=300, null=True, blank=True)
    description = models.TextField("Описание", max_length=1024, null=True, blank=True)

    class Meta:
        verbose_name = u"Образовательная программа"
        verbose_name_plural = u"Образовательные программы"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_EduProgram_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_EduProgram_update", args=(self.pk,))


class ProvidingDiscipline(DateInfo):
    # Relationships
    edu_program = models.ForeignKey("repository.EduProgram", verbose_name="Образовательная программа",
                                    on_delete=models.PROTECT)
    subject = models.ForeignKey("repository.Subject", verbose_name="Дисциплина", on_delete=models.PROTECT)

    # Fields
    rate = models.PositiveIntegerField("Процент покрытия")

    class Meta:
        verbose_name = u"Рекомендация ЦОР в качестве обеспечения дисциплины"
        verbose_name_plural = u"Рекомендации ЦОР в качестве обеспечения дисциплин"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Providing_discipline_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Providing_discipline_update", args=(self.pk,))


class ResultEdu(DateInfo):
    # Fields
    title = models.CharField("Наименование", max_length=150)
    description = models.TextField("Описание", max_length=500)
    digital_resource_competence = models.ForeignKey("repository.DigitalResourceCompetence", verbose_name="Компетенции",
                                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"Образовательный результат"
        verbose_name_plural = u"Образовательные результаты"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_ResultEdu_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_ResultEdu_update", args=(self.pk,))


class DigitalResource(PolymorphicModel):
    # source_data
    MANUAL = '0'
    IMPORT = '1'

    SOURCES = [
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
    authors = models.ManyToManyField("users.Person", verbose_name="Авторы", blank=True,
                                     related_name="authors_digital_resource")
    copyright_holder = models.ForeignKey("Organization", on_delete=models.PROTECT, verbose_name="Правообладатель")
    subjects_tags = models.ManyToManyField("SubjectTag", verbose_name="Тэги дисциплин ЦОР")
    edu_programs_tags = models.ManyToManyField("EduProgramTag", verbose_name="Тэги образовательных программ ЦОР")
    status_cor = models.ForeignKey("DRStatus", on_delete=models.CASCADE, verbose_name="Статус ЦОР")
    owner = models.ForeignKey("users.Person", on_delete=models.PROTECT, related_name="owner_digital_resource",
                              verbose_name="Владелец")
    language = models.ForeignKey("Language", on_delete=models.PROTECT, verbose_name="Язык ресурса")
    provided_disciplines = models.ManyToManyField("ProvidingDiscipline",
                                                  verbose_name="ЦОР рекомендован в качестве обеспечения дисциплины")
    conformity_theme = models.ManyToManyField("ConformityTheme", verbose_name="Соответствие ЦОР темам дисциплины")
    platform = models.ForeignKey("Platform", on_delete=models.PROTECT, verbose_name="Платформа")

    # Fields
    id = models.UUIDField("ID ресурса", primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Наименование ресурса", max_length=150)
    type = models.CharField("Тип ресурса", max_length=30, choices=RESOURCE_TYPE, null=True)
    source_data = models.CharField("Источник данных", max_length=30, choices=SOURCES, default=MANUAL)
    ketwords = models.CharField("Ключевые слова", max_length=100, null=True, blank=True)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)

    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        verbose_name = u"Паспорт ЦОР"
        verbose_name_plural = u"Паспорта ЦОР"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_DigitalResource_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_DigitalResource_update", args=(self.pk,))


class DigitalResourceLinks(DigitalResource):
    URL = models.URLField("Ссылка на файл")
    link_name = models.CharField("Наименование файла", max_length=150, null=True, blank=True)


class DigitalResourceFiles(DigitalResource):
    file = models.FileField(upload_to="upload/files")


class DigitalResourceCompetence(DateInfo):
    digital_resource = models.ForeignKey("repository.DigitalResource", on_delete=models.CASCADE,
                                         verbose_name="Паспорт ЦОР")
    competence = models.ForeignKey("repository.Competence", on_delete=models.PROTECT, verbose_name="Компетенция")

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_DigitalResourceCompetence_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_DigitalResourceCompetence_update", args=(self.pk,))


class Competence(DateInfo):
    # Fields
    title = models.CharField("Наименование", max_length=150)
    code = models.CharField("Код компетенции", max_length=8)

    class Meta:
        verbose_name = u"Компетенция"
        verbose_name_plural = u"Компетенции"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Competence_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Competence_update", args=(self.pk,))


class Platform(DateInfo):
    # Fields
    title = models.CharField("Наимаенование", max_length=150)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    url = models.URLField("Ссылка")
    logo = models.ImageField("Логотп", upload_to="upload/images/", null=True, blank=True)
    contacts = models.TextField("Контакты", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = u"Платформа"
        verbose_name_plural = u"Платформы"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Platform_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Platform_update", args=(self.pk,))


class Language(DateInfo):
    # Fields
    title = models.CharField("Наименование", max_length=80)
    code = models.CharField("Код языка", max_length=4)

    class Meta:
        verbose_name = u"Язык ресура"
        verbose_name_plural = u"Языки ресурсов"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Language_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Language_update", args=(self.pk,))


class SubjectTag(DateInfo):
    # Relationships
    tag = models.ForeignKey("repository.Subject", on_delete=models.CASCADE, verbose_name="Дисциплина")

    class Meta:
        verbose_name = u"Тэг дисциплины"
        verbose_name_plural = u"Тэги дисциплин"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_SubjectTag_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_SubjectTag_update", args=(self.pk,))


class ConformityTheme(DateInfo):
    # Relationships
    theme = models.ForeignKey("repository.SubjectTheme", on_delete=models.CASCADE, verbose_name="Тема дисциплины")
    providing_discipline = models.ForeignKey("repository.ProvidingDiscipline", on_delete=models.CASCADE,
                                             verbose_name="")  # TODO: Должно ли это быть тут ?

    # Fields
    practice = models.NullBooleanField("Практика")
    theory = models.NullBooleanField("Теория")
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        verbose_name = u"Соответствие ЦОР темам дисциплины"
        verbose_name_plural = u"Соответствия ЦОР темам дисциплин"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_ConformityTheme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_ConformityTheme_update", args=(self.pk,))


class EduProgramTag(DateInfo):
    # Relationships
    tag = models.ForeignKey("repository.EduProgram", on_delete=models.CASCADE, verbose_name="Образовательная программа")

    class Meta:
        verbose_name = u"Тэг образовательной программы"
        verbose_name_plural = u"Тэги образовательных программ"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_EduProgramTag_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_EduProgramTag_update", args=(self.pk,))


class SubjectTheme(DateInfo):
    # Fields
    title = models.CharField("Наимаенование", max_length=150)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    thematic_plan = models.ForeignKey("repository.ThematicPlan", on_delete=models.PROTECT,
                                      verbose_name="Тематический план")

    class Meta:
        verbose_name = u"Тема дисциплины"
        verbose_name_plural = u"Темы дисциплин"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_SubjectTheme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_SubjectTheme_update", args=(self.pk,))


class ThematicPlan(DateInfo):

    title = models.CharField("Наименование", max_length=50)
    subject = models.ForeignKey("repository.Subject", on_delete=models.PROTECT, verbose_name="Дисциплина")
    edu_programs = models.ForeignKey("repository.EduProgram", on_delete=models.PROTECT,
                                     verbose_name="Образовательная программа")

    class Meta:
        verbose_name = u"Тематический план"
        verbose_name_plural = u"Тематические планы"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_ThematicPlan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_ThematicPlan_update", args=(self.pk,))
