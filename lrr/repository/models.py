# -*- coding: utf-8 -*-
import uuid

from django.db import models as models
from django.urls import reverse

from lrr.users.models import Person, Student


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        abstract = True


class DRStatus(BaseModel):
    # quality_category
    INNER = 'INNER'
    OUTER = 'OUTER'
    OUTSIDE = 'OUTSIDE'

    QUALITY_CATEGORIES = [
        (INNER, 'внутренний'),
        (OUTER, 'внешний'),
        (OUTSIDE, 'сторонний'),
    ]

    # interactive_category
    NOT_INTERACTIVE = 'NOT_INTERACTIVE'
    WITH_TEACHER_SUPPORT = 'WITH_TEACHER_SUPPORT'
    AUTO = 'AUTO'

    INTERACTIVE_CATEGORIES = [
        (NOT_INTERACTIVE, 'не интерактивный'),
        (WITH_TEACHER_SUPPORT, 'с поддержкой преподавателя'),
        (AUTO, 'автоматизированный'),
    ]

    # Relationships
    expertise_status = models.ForeignKey("repository.ExpertiseStatus", verbose_name="Статус экспертизы",
                                         on_delete=models.CASCADE)
    digital_resource = models.ForeignKey("repository.DigitalResource", verbose_name="Паспорт ЦОР",
                                         on_delete=models.CASCADE)
    edu_program = models.ForeignKey("repository.EduProgram", on_delete=models.PROTECT,
                                    verbose_name="Утвержденная образовательная программа", blank=True, null=True)
    subject = models.ForeignKey("repository.Subject", on_delete=models.PROTECT, verbose_name="Утвержденная дисциплина",
                                blank=True, null=True)

    # Fields
    quality_category = models.CharField("Категория качества", max_length=30, choices=QUALITY_CATEGORIES, blank=True)
    interactive_category = models.CharField("Категория интерактивности", max_length=30, choices=INTERACTIVE_CATEGORIES,
                                            blank=True)

    class Meta:
        verbose_name = u"Статус ЦОР"
        verbose_name_plural = u"Статусы ЦОР"

    def __str__(self):
        return "{} {} {}".format(self.expertise_status, self.get_quality_category_display(),
                                 self.get_interactive_category_display())

    def get_absolute_url(self):
        return reverse("repository:repository_DRStatus_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository:repository_DRStatus_update", args=(self.pk,))


class ExpertiseStatus(BaseModel):
    # status
    NO_INIT = 'NO_INIT'
    SUB_APP = 'SUB_APP'
    ON_EXPERTISE = 'ON_EXPERTISE'
    ON_REVISION = 'ON_REVISION'
    ASSIGNED_STATUS = 'ASSIGNED_STATUS'

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
        return self.get_status_display()

    def get_absolute_url(self):
        return reverse("repository:repository_ExpertiseStatus_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository:repository_ExpertiseStatus_update", args=(self.pk,))


class Subject(BaseModel):
    # Fields
    title = models.CharField("Наименование", max_length=255)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    labor = models.PositiveSmallIntegerField("Трудоемкость", null=True, blank=True)

    class Meta:
        verbose_name = u"Дисциплина"
        verbose_name_plural = u"Дисциплины"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository_Subject_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Subject_update", args=(self.pk,))

    def get_resources(self):
        return DigitalResource.get_resources_by_subject(self)

    def get_recommended_resources(self, edu_program):
        return DigitalResource.get_recommended_resources_by_subject(self, edu_program)


class Organization(BaseModel):
    # Fields
    title = models.CharField("Наименование", max_length=150)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    url_logo = models.URLField("Ссылка на логотип", blank=True, null=True)
    logo = models.ImageField("Логотип", upload_to="upload/images/", null=True, blank=True)
    contacts = models.TextField("Контакты", max_length=500, null=True, blank=True)
    url = models.URLField("URL", null=True, blank=True)

    class Meta:
        verbose_name = u"Организация"
        verbose_name_plural = u"Организации"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository_Organization_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Organization_update", args=(self.pk,))


class EduProgram(BaseModel):
    # Fields
    title = models.CharField("Наименование", max_length=450)
    short_description = models.CharField("Короткое описание", max_length=300, null=True, blank=True)
    description = models.TextField("Описание", max_length=1024, null=True, blank=True)

    class Meta:
        verbose_name = u"Образовательная программа"
        verbose_name_plural = u"Образовательные программы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository_EduProgram_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_EduProgram_update", args=(self.pk,))

    def get_count_resources(self):
        return DigitalResource.objects.filter(edu_programs_tags__tag=self).count()


class ProvidingDiscipline(BaseModel):
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
        return f"{self.edu_program.title} {self.subject.title}"

    def get_absolute_url(self):
        return reverse("repository_Providing_discipline_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Providing_discipline_update", args=(self.pk,))


class ResultEdu(BaseModel):
    # Fields
    title = models.CharField("Наименование", max_length=150)
    description = models.TextField("Описание", max_length=500, blank=True)
    competence = models.ForeignKey("repository.Competence", verbose_name="Компетенция", null=True, blank=True,
                                   on_delete=models.PROTECT)

    class Meta:
        verbose_name = u"Образовательный результат"
        verbose_name_plural = u"Образовательные результаты"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository_ResultEdu_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_ResultEdu_update", args=(self.pk,))


class DigitalResource(BaseModel):
    # source_data
    MANUAL = 'MANUAL'
    IMPORT = 'IMPORT'

    SOURCES = [
        (MANUAL, 'вручную'),
        (IMPORT, 'импорт'),
    ]

    # type
    OK = 'OK'
    EUK = 'EUK'
    TEXT_EOR = 'TEXT_EOR'
    MULTIMEDIA_EOR = 'MULTIMEDIA_EOR'

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
    subjects_tags = models.ManyToManyField("SubjectTag", verbose_name="Тэги дисциплин ЦОР", blank=True)
    edu_programs_tags = models.ManyToManyField("EduProgramTag", verbose_name="Тэги образовательных программ ЦОР",
                                               blank=True)
    owner = models.ForeignKey("users.Person", on_delete=models.PROTECT, related_name="owner_digital_resource",
                              verbose_name="Владелец", blank=True, null=True)
    language = models.ForeignKey("Language", on_delete=models.PROTECT, verbose_name="Язык ресурса")
    provided_disciplines = models.ManyToManyField("ProvidingDiscipline",
                                                  verbose_name="ЦОР рекомендован в качестве обеспечения дисциплины",
                                                  blank=True)
    conformity_theme = models.ManyToManyField("ConformityTheme", verbose_name="Соответствие ЦОР темам дисциплины",
                                              blank=True)
    platform = models.ForeignKey("Platform", on_delete=models.PROTECT, verbose_name="Платформа")
    result_edu = models.ManyToManyField("ResultEdu", verbose_name="Образовательный результат", blank=True)

    # Fields
    title = models.CharField("Наименование ресурса", max_length=1024)
    type = models.CharField("Тип ресурса", max_length=30, choices=RESOURCE_TYPE, null=True)
    source_data = models.CharField("Источник данных", max_length=30, choices=SOURCES, default=MANUAL)
    keywords = models.CharField("Ключевые слова", max_length=6024, null=True, blank=True)
    description = models.TextField("Описание", max_length=6024, null=True, blank=True)

    class Meta:
        verbose_name = u"Паспорт ЦОР"
        verbose_name_plural = u"Паспорта ЦОР"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository:repository_DigitalResource_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository:repository_DigitalResource_update", args=(self.pk,))

    def get_url(self):
        source = self.source_set.first()
        if source:
            return source.URL
        else:
            return ""

    @classmethod
    def get_resources_by_subject(cls, subject):
        if isinstance(subject, Subject):
            tags = SubjectTag.get_by_subject(subject)
            return cls.objects.filter(subjects_tags__in=tags)
        else:
            return None

    @classmethod
    def get_recommended_resources_by_subject(cls, subject, edu_program):
        if isinstance(subject, Subject) and isinstance(edu_program, EduProgram):
            return cls.objects.filter(provided_disciplines__subject=subject,
                                      provided_disciplines__edu_program=edu_program,
                                      drstatus__expertise_status__accepted_status=True)
        else:
            return None

    def get_status(self):
        return self.drstatus_set.all()


class Source(BaseModel):
    link_name = models.CharField("Наименование файла", max_length=150, null=True, blank=True)
    URL = models.URLField("Ссылка", null=True, blank=True)
    file = models.FileField(upload_to="upload/files", null=True, blank=True)
    digital_resource = models.ForeignKey("repository.DigitalResource", verbose_name="Паспорт ЦОР",
                                         on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"Источник"
        verbose_name_plural = u"Источники"

    def get_format(self):
        if self.URL:
            return "url"
        elif self.file:
            return "file"
        else:
            return None


# class DigitalResourceCompetence(BaseModel):
#     digital_resource = models.ForeignKey("repository.DigitalResource", on_delete=models.CASCADE,
#                                          verbose_name="Паспорт ЦОР")
#     competence = models.ForeignKey("repository.Competence", on_delete=models.PROTECT, verbose_name="Компетенция")
#
#     class Meta:
#         verbose_name = u"Паспорт ЦОР / Компетенция"
#         verbose_name_plural = u"Паспорт ЦОР / Компетенции"
#
#     def __str__(self):
#         return "{}".format(self.competence)
#
#     def get_absolute_url(self):
#         return reverse("repository_DigitalResourceCompetence_detail", args=(self.pk,))
#
#     def get_update_url(self):
#         return reverse("repository_DigitalResourceCompetence_update", args=(self.pk,))


class Competence(BaseModel):
    # Fields
    title = models.CharField("Наименование", max_length=150)
    code = models.CharField("Код компетенции", max_length=8)

    class Meta:
        verbose_name = u"Компетенция"
        verbose_name_plural = u"Компетенции"

    def __str__(self):
        return f"{self.code} {self.title}"

    def get_absolute_url(self):
        return reverse("repository_Competence_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Competence_update", args=(self.pk,))


class Platform(BaseModel):
    # Fields
    title = models.CharField("Наименование", max_length=150)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    url = models.URLField("Ссылка")
    url_logo = models.URLField("Ссылка на логотип", null=True, blank=True)
    logo = models.ImageField("Логотип", upload_to="upload/images/", null=True, blank=True)
    contacts = models.TextField("Контакты", max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = u"Платформа"
        verbose_name_plural = u"Платформы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository_Platform_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Platform_update", args=(self.pk,))


class Language(models.Model):
    # Fields

    title = models.CharField("Наименование", max_length=80)
    code = models.CharField("Код языка", max_length=4, primary_key=True)

    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        verbose_name = u"Язык ресура"
        verbose_name_plural = u"Языки ресурсов"

    def __str__(self):
        return self.code

    def get_absolute_url(self):
        return reverse("repository_Language_detail", args=(self.code,))

    def get_update_url(self):
        return reverse("repository_Language_update", args=(self.code,))


class SubjectTag(BaseModel):
    # Relationships
    tag = models.ForeignKey("repository.Subject", on_delete=models.CASCADE, verbose_name="Дисциплина")

    class Meta:
        verbose_name = u"Тэг дисциплины"
        verbose_name_plural = u"Тэги дисциплин"

    def __str__(self):
        return str(self.tag)

    def get_absolute_url(self):
        return reverse("repository_SubjectTag_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_SubjectTag_update", args=(self.pk,))

    @classmethod
    def get_by_subject(cls, subject):
        return cls.objects.filter(tag__title=subject.title)


class ConformityTheme(BaseModel):
    # Relationships
    theme = models.ForeignKey("repository.SubjectTheme", on_delete=models.CASCADE, verbose_name="Тема дисциплины")
    providing_discipline = models.ForeignKey("repository.ProvidingDiscipline", on_delete=models.CASCADE,
                                             verbose_name="Рекомендация ЦОР в качестве обеспечения дисциплины")  # TODO: Должно ли это быть тут ?

    # Fields
    practice = models.NullBooleanField("Практика")
    theory = models.NullBooleanField("Теория")
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        verbose_name = u"Соответствие ЦОР темам дисциплины"
        verbose_name_plural = u"Соответствия ЦОР темам дисциплин"

    def __str__(self):
        return f"{self.theme.title} {self.providing_discipline}"

    def get_absolute_url(self):
        return reverse("repository_ConformityTheme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_ConformityTheme_update", args=(self.pk,))


class EduProgramTag(BaseModel):
    # Relationships
    tag = models.ForeignKey("repository.EduProgram", on_delete=models.CASCADE, verbose_name="Образовательная программа")

    class Meta:
        verbose_name = u"Тэг образовательной программы"
        verbose_name_plural = u"Тэги образовательных программ"

    def __str__(self):
        return str(self.tag)

    def get_absolute_url(self):
        return reverse("repository_EduProgramTag_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_EduProgramTag_update", args=(self.pk,))


class SubjectTheme(BaseModel):
    # Fields
    title = models.CharField("Наимаенование", max_length=150)
    description = models.TextField("Описание", max_length=500, null=True, blank=True)
    thematic_plan = models.ForeignKey("repository.ThematicPlan", on_delete=models.PROTECT,
                                      verbose_name="Тематический план")

    class Meta:
        verbose_name = u"Тема дисциплины"
        verbose_name_plural = u"Темы дисциплин"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository_SubjectTheme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_SubjectTheme_update", args=(self.pk,))


class ThematicPlan(BaseModel):
    title = models.CharField("Наименование", max_length=50)
    subject = models.ForeignKey("repository.Subject", on_delete=models.PROTECT, verbose_name="Дисциплина")
    edu_program = models.ForeignKey("repository.EduProgram", on_delete=models.PROTECT,
                                    verbose_name="Образовательная программа")

    class Meta:
        verbose_name = u"Тематический план"
        verbose_name_plural = u"Тематические планы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository_ThematicPlan_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_ThematicPlan_update", args=(self.pk,))


class WorkPlanAcademicGroup(BaseModel):
    digital_resource = models.ManyToManyField("repository.DigitalResource", verbose_name="Ресурсное обеспечение")
    academic_group = models.ForeignKey("users.AcademicGroup", on_delete=models.PROTECT,
                                       verbose_name="Академическая группа")
    edu_program = models.ForeignKey("repository.EduProgram", on_delete=models.PROTECT,
                                    verbose_name="Образовательная программа")
    subject = models.ManyToManyField("repository.Subject", verbose_name="Дисциплины")
    semestr = models.PositiveSmallIntegerField("Семестр", null=True, blank=True)

    class Meta:
        verbose_name = u"Ресурсное обеспечение академической группы"
        verbose_name_plural = u"Ресурсное обеспечение академических групп"

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_WorkPlanAcademicGroup_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_WorkPlanAcademicGroup_update", args=(self.pk,))

    def get_resources_by_subject(self):
        return DigitalResource.get_resources_by_subject(self.subject)
