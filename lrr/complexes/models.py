# -*- coding: utf-8 -*-
import logging

from django.db import models
from django.urls import reverse
from polymorphic.models import PolymorphicModel

from lrr.repository.models import BaseModel, Subject, Direction, Competence, ResultEdu, DigitalResource, Language, \
    Platform
from lrr.users.models import Person

logger = logging.getLogger(__name__)


class DigitalComplex(BaseModel):
    title = models.CharField("Наименогвание комплекса", max_length=150, blank=True, null=True)
    subjects = models.ManyToManyField(Subject, verbose_name="Дисциплина(ы)", blank=True)
    directions = models.ManyToManyField(Direction, verbose_name="Направления подготовки", blank=True)
    description = models.TextField('Описание', blank=True)
    competences = models.ManyToManyField(Competence, verbose_name="Компетенции", blank=True)
    results_edu = models.ManyToManyField(ResultEdu, verbose_name="Результаты обучения", blank=True)
    digital_resources = models.ManyToManyField(DigitalResource, verbose_name="Компоненты ЭУМК")
    format = models.CharField("Формат использования", max_length=300, blank=True)
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

    def get_digital_complex(self):
        digital_complex_pk = self.request.path.split('/')[4]
        digital_complex = DigitalComplex.objects.get(pk=digital_complex_pk)
        return digital_complex

    @classmethod
    def get_count_complex(cls):
        return cls.objects.all().count()


class Cell(BaseModel):
    ASYNC = 'ASYNC'
    SYNC = 'SYNC'

    CELL_TYPE = [
        (ASYNC, 'асинхронные мероприятия'),
        (SYNC, 'синхронные мероприятия'),
    ]

    type = models.CharField("Тип ячейки", max_length=50, choices=CELL_TYPE, null=True)
    include_practice = models.BooleanField("Практика", blank=True, null=True)
    include_theory = models.BooleanField("Теория", blank=True, null=True)
    beg_theme_number = models.PositiveSmallIntegerField("Начало диапазонов объединяемых строчек", blank=True)
    end_theme_number = models.PositiveSmallIntegerField("Конец диапазонов объединяемых строчек", blank=True)
    methodology_description = models.CharField("Методологическое описание", max_length=1024, blank=True)

    class Meta:
        verbose_name = u"Ячейка цифрового комплекса ЭУМК"
        verbose_name_plural = u"Ячейки цифрового комплекса ЭУМК"

    def __str__(self):
        return self.get_type_display()


class ComplexSpaceCell(BaseModel):
    digital_complex = models.ForeignKey("complexes.DigitalComplex", verbose_name="Комплекс ЭМУК",
                                        on_delete=models.CASCADE, blank=True)
    title = models.CharField("Наимаенование", max_length=150)
    cells = models.ManyToManyField(Cell, verbose_name="Ячейка комплекса", blank=True)
    description = models.TextField("Описание", max_length=300)
    link = models.URLField("Ссылка на образовательное пространство", blank=True, null=True)

    class Meta:
        verbose_name = u"Компонент ячейки комплекса"
        verbose_name_plural = u"Компоненты ячеек комплекса"

    def __str__(self):
        return str(self.title)


class RegistryStatus(BaseModel):
    experise_date = models.DateTimeField("Дата экспертизы", editable=True, blank=True)
    relevance_date = models.DateTimeField("Дата обновления экспертизы", editable=True, blank=True)
    digital_complex = models.ForeignKey("complexes.DigitalComplex", verbose_name="Комплекс ЭМУК",
                                        on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = u"Статус экспертизы комплекса"
        verbose_name_plural = u"Статусы экспертизы комплекса"


class RegistryStatusProgSubject(BaseModel):
    coverage_procentage = models.PositiveSmallIntegerField("Процент покрытия", blank=True)
    subject = models.ForeignKey(Subject, verbose_name="Дисциплина", on_delete=models.CASCADE, blank=True, null=True)
    edu_program = models.ForeignKey("repository.EduProgram", on_delete=models.CASCADE,
                                    verbose_name="Образовательная программа", blank=True, null=True)
    status = models.ForeignKey("complexes.RegistryStatus", verbose_name="Статус экспертизы комплекса",
                               on_delete=models.PROTECT, blank=True)

    class Meta:
        verbose_name = u"Соответсвие статуса комплекса, с дисциплинами и программами"
        verbose_name_plural = u"Соответсвие статуса комплекса, с дисциплинами и программами"


class ComplexTheme(BaseModel):
    title = models.CharField("Наимаенование", max_length=150)
    number = models.PositiveSmallIntegerField("Номер темы", blank=True)
    digital_complex = models.ForeignKey("complexes.DigitalComplex", verbose_name="Комплекс ЭМУК",
                                        on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = u"Тема карты комплекса"
        verbose_name_plural = u"Темы карты комплекса"


class CellWeeks(BaseModel):
    cell = models.ForeignKey('complexes.Cell', verbose_name="Ячейка комплекса", on_delete=models.CASCADE, blank=True)
    beg_week_number = models.PositiveSmallIntegerField("Начало диапазона недель учебного графика ячейки", blank=True)
    end_week_number = models.PositiveSmallIntegerField("Конец диапазона недель учебного графика ячейки", blank=True)
    edu_form = models.CharField("Форма обучения для которой сотавлен график", max_length=150, blank=True)

    class Meta:
        verbose_name = u"Неделя календарного учебного графика"
        verbose_name_plural = u"Недели календарного учебного графика"

    def __str__(self):
        return str(self.edu_form)


class WorkPlanAcademicGroup(BaseModel):
    digital_complex = models.ManyToManyField("complexes.DigitalComplex", verbose_name="Ресурсное обеспечение")
    academic_group = models.ForeignKey("users.AcademicGroup", on_delete=models.PROTECT,
                                       verbose_name="Академическая группа")
    direction = models.ForeignKey("repository.Direction", on_delete=models.PROTECT,
                                  verbose_name="Направление подготовки", null=True)
    subject = models.ForeignKey("repository.Subject", verbose_name="Дисциплины", on_delete=models.PROTECT, null=True)
    learn_date = models.PositiveSmallIntegerField("Учебный год", null=True, blank=True)
    semestr = models.PositiveSmallIntegerField("Семестр", null=True, blank=True)

    class Meta:
        verbose_name = u"Ресурсное обеспечение академической группы"
        verbose_name_plural = u"Ресурсное обеспечение академических групп"

    def __str__(self):
        return str(self.academic_group)

    def get_absolute_url(self):
        return reverse("repository_WorkPlanAcademicGroup_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_WorkPlanAcademicGroup_update", args=(self.pk,))


class ComponentComplex(BaseModel, PolymorphicModel):
    digital_complex = models.ForeignKey(DigitalComplex, verbose_name="ЭУМК", on_delete=models.CASCADE, blank=True)
    description = models.CharField("Описание / Методика применения", max_length=1024, blank=True, null=True)

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
    pass


class PlatformComponent(ComponentComplex):
    platform = models.ForeignKey(Platform, verbose_name="Платформа", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.platform.title

    def get_absolute_url(self):
        return reverse("complexes:complexes_ComponentComplex_create", args=(self.digital_complex.pk,))

    class Meta:
        verbose_name = 'Компонент платформы'
        verbose_name_plural = 'Компоненты платформ'


class TraditionalSessionComponent(ComponentComplex):
    title = models.CharField("Наименование вида занятий", max_length=150, blank=True)
    description_session = models.TextField("Описание занятий", max_length=2024, blank=True)
    url = models.URLField("Ссылка на онлайн-расписание занятий", null=True, blank=True)

    def get_absolute_url(self):
        return reverse("complexes:complexes_ComponentComplex_create", args=(self.digital_complex.pk,))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'компонент традиционных занятий'
        verbose_name_plural = 'компоненты традиционных занятий'
