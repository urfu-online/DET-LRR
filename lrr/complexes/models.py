# -*- coding: utf-8 -*-
import logging

from django.contrib.postgres.fields import IntegerRangeField
from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from lrr.repository.models import BaseModel, Subject, Direction, Competence, ResultEdu, DigitalResource, Language, \
    Platform
from lrr.users.models import Person, Student, AcademicGroup
from .grid_models import *
logger = logging.getLogger(__name__)


class DigitalComplex(Complex, BaseModel):
    FORMAT_TYPES = (
        ("0", "смешанное обучение (Ауд+Дист+ЭИОС)"),
        ("1", "смешанное обучение (Ауд+Дист)"),
        ("2", "смешанное обучение (Ауд+ЭИОС)"),
        ("3", "дистанционное обучение (Дист+ЭИОС)"),
        ("4", "дистанционное обучение (Дист)"),
        ("5", "исключительно электронное обучение"),
        ("6", "традиционное обучение"),
    )
    title = models.CharField("Наименование комплекса", max_length=150, blank=True, null=True, default="", db_index=True)
    subjects = models.ManyToManyField(Subject, verbose_name="Дисциплина(ы)", blank=True)
    directions = models.ManyToManyField(Direction, verbose_name="Направления подготовки", blank=True)
    description = models.TextField('Описание', blank=True)
    competences = models.ManyToManyField(Competence, verbose_name="Компетенции", blank=True)
    results_edu = models.ManyToManyField(ResultEdu, verbose_name="Результаты обучения", blank=True)
    format = models.CharField("Формат использования", choices=FORMAT_TYPES, max_length=300, blank=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, verbose_name="Язык комплекса")
    keywords = models.CharField("Ключевые слова", max_length=300, null=True, blank=True)
    owner = models.ForeignKey(Person, on_delete=models.PROTECT, related_name="owner_digital_complex",
                              verbose_name="Владелец", blank=True, null=True)

    class Meta:
        verbose_name = u"Цифровой Комплекс (ЭУМК)"
        verbose_name_plural = u"Цифровые Комплексы (ЭУМК)"

    def __str__(self):
        return f"{self.title}/{self.keywords}"

    def get_absolute_url(self):
        return reverse("complexes:complexes_DigitalComplex_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("complexes:complexes_DigitalComplex_update", args=(self.pk,))

    def get_owner(self, user):
        try:
            if self.owner.user == user:
                return True
            else:
                return False
        except:
            return False

    @classmethod
    def get_count_complex(cls):
        return cls.objects.count()


# class Cell(BaseModel):
#     ASYNC = 'ASYNC'
#     SYNC = 'SYNC'
#
#     CELL_TYPE = [
#         (ASYNC, 'асинхронные мероприятия'),
#         (SYNC, 'синхронные мероприятия'),
#     ]
#
#     type = models.CharField("Тип ячейки", max_length=50, choices=CELL_TYPE, null=True)
#     include_practice = models.BooleanField("Практика", blank=True, null=True)
#     include_theory = models.BooleanField("Теория", blank=True, null=True)
#     week_range = IntegerRangeField("Диапозон ", blank=True, null=True)
#     methodology_description = models.CharField("Методологическое описание", max_length=1024, blank=True, null=True)
#     component_complexes = models.ManyToManyField("complexes.ComponentComplex", verbose_name="Компоненты ЭУМК",
#                                                  blank=True)
#
#     class Meta:
#         verbose_name = u"Ячейка цифрового комплекса ЭУМК"
#         verbose_name_plural = u"Ячейки цифрового комплекса ЭУМК"
#
#     def __str__(self):
#         return self.get_type_display()


# class ComplexSpaceCell(BaseModel):
#     digital_complex = models.ForeignKey("complexes.DigitalComplex", verbose_name="Комплекс ЭУМК",
#                                         on_delete=models.CASCADE, blank=True, null=True)
#     theme_name = models.CharField("Тема / Раздел", max_length=1024, blank=True, null=True)
#     cell_json = models.JSONField("Координаты ячеек", blank=True, null=True)
#
#     class Meta:
#         verbose_name = u"Компонент ячейки комплекса"
#         verbose_name_plural = u"Компоненты ячеек комплекса"
#
#     def __str__(self):
#         return self.theme_name


class AssignmentAcademicGroup(BaseModel):
    FIRST = 'FIRST'
    SECOND = 'SECOND'

    NUMBER_SEMESTR_TYPE = [
        (FIRST, 'Первый семестр'),
        (SECOND, 'Второй семестр'),
    ]
    digital_complex = models.ForeignKey("complexes.DigitalComplex", verbose_name="ЭУМКи", on_delete=models.CASCADE,
                                        blank=True, null=True)
    academic_group = models.ForeignKey(AcademicGroup, on_delete=models.PROTECT,
                                       verbose_name="Академическая группа", blank=True, null=True)
    subject = models.ForeignKey("repository.Subject", verbose_name="Дисциплина", blank=True, on_delete=models.PROTECT,
                                null=True)
    learn_date = models.PositiveSmallIntegerField("Учебный год", null=True, blank=True)
    semestr = models.CharField("Семестр", max_length=12, choices=NUMBER_SEMESTR_TYPE, null=True, blank=True)

    class Meta:
        verbose_name = u"Ресурсное обеспечение академической группы"
        verbose_name_plural = u"Ресурсное обеспечение академических групп"

    def __str__(self):
        return f"{self.academic_group} {self.subject} {self.learn_date} {self.semestr}"

    # def get_absolute_url(self):
    #     return reverse("complexes:complexes_AssignmentAcademicGroup_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("complexes:complexes_AssignmentAcademicGroup_update", args=(self.pk,))

    @classmethod
    def get_assignment_group_digital_complex(cls, request):
        digital_complex_pk = request.path.split('/')[4]
        return cls.objects.filter(digital_complex__pk=digital_complex_pk)


class ComponentComplex(BaseModel, PolymorphicModel):
    digital_complex = models.ForeignKey(DigitalComplex, verbose_name="ЭУМК", on_delete=models.CASCADE, blank=True)
    description = models.TextField("Описание / Методика применения", max_length=1024, blank=True, null=True)
    order = models.IntegerField("Порядрок отображения компонента", blank=True, null=True)

    def __str__(self):
        return f"{self.digital_complex.title} - {self.digital_complex.keywords} - {self.digital_complex.format}"

    def get_absolute_url(self):
        return reverse("complexes:complexes_DigitalComplex_detail", args=(self.digital_complex.pk,))

    class Meta:
        verbose_name = 'компонент комплекса'
        verbose_name_plural = 'компоненты комплексов'


class ResourceComponent(ComponentComplex):
    digital_resource = models.ForeignKey(DigitalResource, verbose_name="ЭОР", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.digital_resource.title

    def get_absolute_url(self):
        return reverse("complexes:complexes_ComponentComplex_create", args=(self.digital_complex.pk,))

    class Meta:
        verbose_name = 'Компонент ЭОР'
        verbose_name_plural = 'Компоненты ЭОР'


class LiterarySourcesComponent(ComponentComplex):
    title = models.CharField("Библиографическая ссылка", max_length=424, null=True, blank=True)
    url = models.URLField("URL", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("complexes:complexes_ComponentComplex_create", args=(self.digital_complex.pk,))

    class Meta:
        verbose_name = 'Литературный источник'
        verbose_name_plural = 'Литературные источники'


class PlatformComponent(ComponentComplex):
    title = models.CharField("Наименование", max_length=150, blank=True)
    description_self = models.TextField("Описание", max_length=2024, blank=True)
    url = models.URLField("Ссылка на онлайн-расписание занятий", null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("complexes:complexes_ComponentComplex_create", args=(self.digital_complex.pk,))

    class Meta:
        verbose_name = 'Среда обучения'
        verbose_name_plural = 'Среда обучения'


class TraditionalSessionComponent(ComponentComplex):
    title = models.CharField("Наименование вида занятий", max_length=150, blank=True)
    description_session = models.TextField("Описание занятий", max_length=2024, blank=True)
    url = models.URLField("Ссылка на онлайн-расписание занятий", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("complexes:complexes_ComponentComplex_create", args=(self.digital_complex.pk,))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Синхронное занятие'
        verbose_name_plural = 'Синхронные занятия'
