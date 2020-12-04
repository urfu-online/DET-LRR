# -*- coding: utf-8 -*-
from django.db import models as models

from lrr.repository.models import BaseModel, Subject, Direction, Competence, ResultEdu, DigitalResource, Language


class DigitalComplex(BaseModel):
    subjects = models.ManyToManyField(Subject, verbose_name="Дисциплина(ы)", blank=True)
    directions = models.ManyToManyField(Direction, verbose_name="Направления подготовки", blank=True)
    description = models.TextField('Описание', blank=True)
    competences = models.ManyToManyField(Competence, verbose_name="Компетенции", blank=True)
    results_edu = models.ManyToManyField(ResultEdu, verbose_name="Результаты обучения", blank=True)
    digital_resources = models.ManyToManyField(DigitalResource, verbose_name="Компоненты ЭУМК")
    format = models.CharField("Формат использования", max_length=300, blank=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT, verbose_name="Язык комплекса")
    keywords = models.CharField("Ключевые слова", max_length=300, null=True, blank=True)
    space_cell = models.ForeignKey("complexes.ComplexSpaceCell", verbose_name="Структурно-тематический план",
                                   on_delete=models.PROTECT)

    class Meta:
        verbose_name = u"Цифровой Комплекс (ЭУМК)"
        verbose_name_plural = u"Цифровые Комплексы (ЭУМК)"


class Cell(BaseModel):
    ASYNC = 'ASYNC'
    SYNC = 'SYNC'

    CELL_TYPE = [
        (ASYNC, 'асинхронные мероприятия'),
        (SYNC, 'синхронные мероприятия'),
    ]

    type = models.CharField("Тип ячейки", max_length=50, choices=CELL_TYPE, null=True)
    include_practice = models.NullBooleanField("Практика", blank=True)
    include_theory = models.NullBooleanField("Теория", blank=True)
    beg_theme_number = models.PositiveSmallIntegerField("Начало диапазонов объединяемых строчек", blank=True)
    end_theme_number = models.PositiveSmallIntegerField("Конец диапазонов объединяемых строчек", blank=True)
    methodology_description = models.CharField("Методологическое описание", max_length=1024, blank=True)

    class Meta:
        verbose_name = u"Ячейка цифрового комплекса ЭУМК"
        verbose_name_plural = u"Ячейки цифрового комплекса ЭУМК"


class ComplexSpaceCell(BaseModel):
    title = models.CharField("Наимаенование", max_length=150)
    cells = models.ManyToManyField(Cell, verbose_name="Ячейка комплекса", blank=True)
    description = models.TextField("Описание", max_length=300)

    # TODO: Уточнить поля
    # link

    class Meta:
        verbose_name = u"Компонент ячейки комплекса"
        verbose_name_plural = u"Компоненты ячеек комплекса"


# TODO: уточнить что за статусы реестра RegistryStatus и RegistryStatusProgSubject
class RegistryStatus(BaseModel):
    experise_date = models.DateTimeField("Дата экспертизы", editable=True, blank=True)
    relevance_date = models.DateTimeField("Дата обнавления экспертизы", editable=True, blank=True)

    # TODO: RegistryStatusProgSubject ForeignKey ??

    class Meta:
        verbose_name = u"Статус рееста"
        verbose_name_plural = u"Статусы реестра"


class RegistryStatusProgSubject(BaseModel):
    coverage_procentage = models.PositiveSmallIntegerField("Процент покрытия", blank=True)
    subject = models.ForeignKey(Subject, verbose_name="Дисциплина", on_delete=models.PROTECT, blank=True, null=True)
    edu_program = models.ForeignKey("repository.EduProgram", on_delete=models.PROTECT,
                                    verbose_name="Образовательная программа", blank=True, null=True)

    class Meta:
        verbose_name = u"Процент покрытия "
        verbose_name_plural = u"Статусы ЭОР"


class ComplexTheme(BaseModel):
    title = models.CharField("Наимаенование", max_length=150)
    number = models.PositiveSmallIntegerField("Номер темы", blank=True)

    class Meta:
        verbose_name = u"Тема карты комплекса"
        verbose_name_plural = u"Темы карты комплекса"
