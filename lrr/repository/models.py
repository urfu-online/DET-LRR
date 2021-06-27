# -*- coding: utf-8 -*-
import logging
import uuid

from django.conf import settings
# from lrr.users.models import Person
from django.contrib.postgres.fields import ArrayField
from django.db import models as models
from django.db import transaction
from django.urls import reverse

logger = logging.getLogger(__name__)


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        abstract = True


class Subject(BaseModel):
    # Fields
    title = models.CharField("Наименование", max_length=255, db_index=True)
    description = models.TextField("Описание", null=True, blank=True)
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

    def get_recommended_resources(self):
        return DigitalResource.get_recommended_resources_by_subject(self)


class Organization(BaseModel):
    # Fields
    title = models.CharField("Наименование", max_length=150, db_index=True)
    description = models.TextField("Описание", null=True, blank=True)
    url_logo = models.URLField("Ссылка на логотип", blank=True, null=True)
    logo = models.ImageField("Логотип", upload_to="upload/images/", null=True, blank=True)
    contacts = models.TextField("Контакты", null=True, blank=True)
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


class ScientificBranch(BaseModel):
    title = models.CharField("Наименование", max_length=64)
    code = models.PositiveSmallIntegerField("Код", blank=True, null=True, unique=True)

    class Meta:
        verbose_name = u"научная отрасль"
        verbose_name_plural = u"научные отрасли"

    def __str__(self):
        return f"{self.code} {self.title}"


class DirectionsEnlargedGroup(BaseModel):
    """
    AreaEducation
    """
    title = models.CharField("Наименование УГН", max_length=128)
    code = models.CharField("Код УГН", max_length=64, unique=True)

    class Meta:
        verbose_name = u"укрупненная группа направлений"
        verbose_name_plural = u"укрупненные группа направлений"

    def __str__(self):
        return f"{self.code} {self.title}"


class Direction(BaseModel):
    uni_id = models.CharField(db_index=True, max_length=64, null=True, blank=True)
    title = models.CharField("Наименование", max_length=150, db_index=True)
    code = models.CharField("Код направления", max_length=8, db_index=True)
    scientific_branch = models.ForeignKey(ScientificBranch, verbose_name="Научная отрасль", related_name="directions",
                                          null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"Направление подготовки"
        verbose_name_plural = u"Направления подготовки"

    def __str__(self):
        return f"{self.code} {self.title}"

    def get_absolute_url(self):
        return reverse("repository_Competence_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Competence_update", args=(self.pk,))

    @classmethod
    def by_code(cls, code):
        qs = cls.objects.filter(code=code)
        if qs.exists():
            return qs[0]
        else:
            return None


class EduProgram(BaseModel):
    STANDARDS = (
        ("SUOS", "СУОС"),
        ("FGOS3++", "ФГОС 3++"),
        ("FGOS VO", "ФГОС ВО"),
    )

    LEVELS = (
        ("0", "бакалавриат"),
        ("1", "прикладной бакалавриат"),
        ("2", "магистратура"),
        ("3", "аспирантура"),
        ("4", "специалитет"),
    )
    # NO_INIT = 'NO_INIT'
    # SUB_APP = 'SUB_APP'
    # ON_EXPERTISE = 'ON_EXPERTISE'
    # ON_REVISION = 'ON_REVISION'
    # ASSIGNED_STATUS = 'ASSIGNED_STATUS'
    #
    # LEVEL_EDU_TYPES = [
    #     (NO_INIT, 'не инициирована'),
    #     (SUB_APP, 'подана заявка'),
    #     (ON_EXPERTISE, 'на экспертизе'),
    #     (ON_REVISION, 'на доработку'),
    #     (ASSIGNED_STATUS, 'присвоен статус'),
    #     # Fields
    #
    # ]

    # Fields
    title = models.CharField("Наименование", max_length=450, db_index=True)
    _cipher = models.CharField("Шифр ОП", max_length=5, blank=True, null=True)
    short_description = models.CharField("Короткое описание", max_length=300, null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)
    standard = models.CharField("Стандарт", max_length=9, null=True, blank=True)
    edu_level = models.CharField("Уровень подготовки", max_length=32, null=True, blank=True)

    admission_years = ArrayField(models.PositiveSmallIntegerField(blank=True, null=True), null=True)
    approve_year = models.PositiveSmallIntegerField("Год утверждения", blank=True, null=True)

    head = models.CharField("Руководитель", max_length=300, null=True, blank=True)
    site_admin = models.CharField("Администратор сайта ОП", max_length=300, null=True, blank=True)

    direction = models.ForeignKey(Direction, verbose_name="Направление подготовки", related_name="programs", null=True,
                                  blank=True, on_delete=models.CASCADE)

    @property
    def cipher(self):
        try:
            c, d = self._cipher, self.direction.code
            return f"{d}/{c}"
        except:
            return ""

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


class ResultEdu(BaseModel):
    # Fields
    title = models.CharField("Наименование", max_length=150, db_index=True)
    description = models.TextField("Описание", blank=True)
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


from django.utils.functional import cached_property


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
    subjects_tags = models.ManyToManyField("SubjectTag", verbose_name="Тэги дисциплин ЭОР", blank=True)
    edu_programs_tags = models.ManyToManyField("EduProgramTag", verbose_name="Тэги образовательных программ ЭОР",
                                               blank=True)
    owner = models.ForeignKey("users.Person", on_delete=models.PROTECT, related_name="owner_digital_resource",
                              verbose_name="Владелец", blank=True, null=True)
    language = models.ForeignKey("Language", on_delete=models.PROTECT, verbose_name="Язык ресурса")
    platform = models.ForeignKey("Platform", on_delete=models.PROTECT, verbose_name="Платформа")
    result_edu = models.ManyToManyField("ResultEdu", verbose_name="Образовательный результат", blank=True)
    competences = models.ManyToManyField("Competence", verbose_name="Компетенции", blank=True)

    # Fields
    title = models.CharField("Наименование ресурса", max_length=1024, db_index=True)
    type = models.CharField("Тип ресурса", max_length=30, choices=RESOURCE_TYPE, null=True)
    source_data = models.CharField("Источник данных", max_length=30, choices=SOURCES, default=MANUAL)
    keywords = models.CharField("Ключевые слова", max_length=6024, null=True, blank=True)
    description = models.TextField("Описание", null=True, blank=True)

    class Meta:
        verbose_name = u"Паспорт ЭОР"
        verbose_name_plural = u"Паспорта ЭОР"
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository:repository_DigitalResource_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository:repository_DigitalResource_update", args=(self.pk,))

    @cached_property
    def get_url(self):
        # if  self.source_set.exists():
        source_set = self.source_set
        if self.source_set.exists():
            return source_set.first().URL
        else:
            return ""

    def get_create_expertise_url(self):
        return reverse("inspections:inspections_Expertise_create", args=(self.pk,))

    def get_source(self):
        try:
            obj = self.source_set  # Source.objects.filter(digital_resource=self)
        except:
            obj = None
        return obj

    @classmethod
    def get_resources_by_subject(cls, subject):
        if isinstance(subject, Subject):
            tags = SubjectTag.get_by_subject(subject)
            return cls.objects.filter(subjects_tags__in=tags)
        else:
            return None

    @classmethod
    def get_recommended_resources_by_subject(cls, subject):
        if isinstance(subject, Subject):
            return cls.objects.filter(provided_disciplines__subject=subject, expertise__status='ASSIGNED_STATUS')
        else:
            return None

    def get_owner(self, user):
        try:
            if self.owner.user == user:
                return True
            else:
                return False
        except:
            return False

    @classmethod
    def get_stats_by_type(cls):
        return {
            'Онлайн-курс': cls.objects.filter(type=cls.OK).count(),
            'ЭУК': cls.objects.filter(type=cls.EUK).count(),
            'Текстовый электронный образовательный ресурс': cls.objects.filter(type=cls.TEXT_EOR).count(),
            'Мультимедийный электронный образовательный ресурс': cls.objects.filter(type=cls.MULTIMEDIA_EOR).count(),
        }


class SourceManager(models.Manager):
    def update_type(self, sources):
        for source in sources:
            source.update_type()


class Source(BaseModel):
    # type
    URL = 'URL'
    FILE = 'FILE'

    SOURCE_TYPE = [
        (URL, 'Ссылочный'),
        (FILE, 'Файл'),
    ]
    link_name = models.CharField("Наименование", max_length=150, null=True, blank=True)
    URL = models.URLField("Ссылка", null=True, blank=True)
    file = models.FileField(verbose_name="Файл", upload_to="upload/files", null=True, blank=True)
    digital_resource = models.ForeignKey("repository.DigitalResource", verbose_name="Паспорт ЭОР",
                                         on_delete=models.CASCADE)
    type = models.CharField("Тип", choices=SOURCE_TYPE, max_length=150, null=True, blank=True)

    class Meta:
        verbose_name = u"Компонент"
        verbose_name_plural = u"Компоненты"

    @transaction.atomic
    def update_type(self):
        if not self.type:
            if self.URL and self.file:
                logging.info(f"Source {self.pk} have ambiguous type")
            elif self.URL and not self.file:
                self.type = 'URL'
                self.save()
            elif self.file and not self.URL:
                self.type = 'file'
                self.save()
            logging.info(f"Source {self.pk} type updated")

    @property
    def get_link_name(self):
        if self.link_name:
            return self.link_name
        return settings.DEFAULT_SOURCE_NAME

    def __str__(self):
        return f"Компонент: {self.digital_resource.title}.{self.get_format()}"

    def get_format(self):
        if self.URL:
            return "url"
        elif self.file:
            return "file"
        else:
            return None


# class DigitalResourceCompetence(BaseModel):
#     digital_resource = models.ForeignKey("repository.DigitalResource", on_delete=models.CASCADE,
#                                          verbose_name="Паспорт ЭОР")
#     competence = models.ForeignKey("repository.Competence", on_delete=models.PROTECT, verbose_name="Компетенция")
#
#     class Meta:
#         verbose_name = u"Паспорт ЭОР / Компетенция"
#         verbose_name_plural = u"Паспорт ЭОР / Компетенции"
#
#     def __str__(self):
#         return "{}".format(self.competence)
#
#     def get_absolute_url(self):
#         return reverse("repository_DigitalResourceCompetence_detail", args=(self.pk,))
#
#     def get_update_url(self):
#         return reverse("repository_DigitalResourceCompetence_update", args=(self.pk,))
class CompetenceGroup(models.Model):
    name = models.CharField("Наименование", max_length=400, db_index=True)

    def __str__(self):
        return self.name


class Competence(BaseModel):
    TYPES = ("ОК", "ОПК", "ПК", "ПСК", "УК", "ДОК", "ДОПК", "ДПК")
    # Fields
    title = models.CharField("Наименование", max_length=150)
    code = models.CharField("Код", max_length=8)
    okso = models.CharField("Код", max_length=8, null=True)

    # TODO: add fields
    # type choices_to TYPES
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
    title = models.CharField("Наименование", max_length=150, db_index=True)
    description = models.TextField("Описание", null=True, blank=True)
    url = models.URLField("Ссылка")
    url_logo = models.URLField("Ссылка на логотип", null=True, blank=True)
    logo = models.ImageField("Логотип", upload_to="upload/images/", null=True, blank=True)
    contacts = models.TextField("Контакты", null=True, blank=True)

    class Meta:
        verbose_name = u"Платформа"
        verbose_name_plural = u"Платформы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository:repository_Platform_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository:repository_Platform_update", args=(self.pk,))


class Language(models.Model):
    # Fields

    title = models.CharField("Наименование", max_length=80, db_index=True)
    code = models.CharField("Код языка", max_length=4, primary_key=True)

    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    class Meta:
        verbose_name = u"Язык ресура"
        verbose_name_plural = u"Языки ресурсов"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("repository_Language_detail", args=(self.code,))

    def get_update_url(self):
        return reverse("repository_Language_update", args=(self.code,))


# TODO: Карасик спросил для чего эта модель
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


class BookmarkBase(models.Model):
    class Meta:
        abstract = True

    user = models.ForeignKey("users.User", verbose_name="Пользователь", on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    def __str__(self):
        return self.user.username


class BookmarkDigitalResource(BookmarkBase):
    class Meta:
        db_table = "bookmark__digital_resource"

    obj = models.ForeignKey('repository.DigitalResource', verbose_name="Паспорт ЭОР", on_delete=models.CASCADE)
