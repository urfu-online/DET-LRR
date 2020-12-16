# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-

from django.db import models as models
from django.urls import reverse

from lrr.complexes import models as complex_model
from lrr.repository import models as repository_model
from lrr.users.models import Person, Expert


class Expertise(repository_model.BaseModel):
    NO_INIT = 'NO_INIT'
    SUB_APP = 'SUB_APP'
    ON_EXPERTISE = 'ON_EXPERTISE'
    ON_REVISION = 'ON_REVISION'
    ASSIGNED_STATUS = 'ASSIGNED_STATUS'
    NOT_ASSIGNED_STATUS = 'NOT_ASSIGNED_STATUS'

    STATUS_CHOICES = [
        (SUB_APP, 'подана заявка'),
        (ON_EXPERTISE, 'на экспертизе'),
        (ON_REVISION, 'на доработку'),
        (ASSIGNED_STATUS, 'присвоен статус'),
        (NOT_ASSIGNED_STATUS, 'не присвоен статус'),
        # Fields

    ]

    digital_resource = models.ForeignKey(repository_model.DigitalResource, verbose_name="Паспорт ЭОР",
                                         on_delete=models.CASCADE)
    date = models.DateTimeField("Дата заявки")
    subjects = models.ManyToManyField(repository_model.Subject, verbose_name="Дисциплина(ы)", blank=True)
    direction = models.ForeignKey(repository_model.Direction, verbose_name="Направление подготовки",
                                  on_delete=models.CASCADE)
    digital_complex = models.ForeignKey(complex_model.DigitalComplex, verbose_name="ЭУМК", on_delete=models.PROTECT)
    expert = models.ManyToManyField(Expert, verbose_name="Назначенные эксперты ", blank=True)
    date_end = models.DateTimeField("До какого действует статус экспертизы")
    file = models.FileField(
        verbose_name="№ протокола комиссии по ресурсному обеспечению модулей и ЭО методического совета",
        upload_to="upload/files", null=True, blank=True)
    remarks = models.TextField("Замечания и рекомендации комиссии")
    status = models.CharField("Состояние экспертизы", max_length=30, choices=STATUS_CHOICES,
                              default=NOT_ASSIGNED_STATUS)

    class Meta:
        verbose_name = u"Экспертиза"
        verbose_name_plural = u"Экспертизы"

    def __str__(self):
        return self.get_status_display()

    def get_absolute_url(self):
        return reverse("inspections:inspections_Expertise_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("inspections:inspections_Expertise_update", args=(self.pk,))


class CheckList(repository_model.BaseModel):
    # status
    METHODIGAL = 'METHODIGAL'
    CONTENT = 'CONTENT'
    TECH = 'TECH'
    NO_TYPE = 'NO_TYPE'

    TYPE_CHOICES = [
        (METHODIGAL, 'Методическая'),
        (CONTENT, 'Содержательная'),
        (TECH, 'Техническая'),
        (NO_TYPE, 'Отсутствует тип экспертизы')
        # Fields

    ]

    type = models.CharField("Тип чек-листа", max_length=30, choices=TYPE_CHOICES, default=NO_TYPE)
    expert = models.ForeignKey(Expert, verbose_name="Эксперт", on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField("Дата проведения экспертизы")
    protocol = models.CharField("№ Протокола учебно-методического совета института", max_length=424)
    expertise = models.ForeignKey(Expertise, verbose_name="Экспертиза", on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = u"Чек-лист экспертизы"
        verbose_name_plural = u"Чек-листы экспертиз"

    def __str__(self):
        return self.get_type_display()

    def get_absolute_url(self):
        return reverse("inspections:inspections_CheckList_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("inspections:inspections_CheckList_update", args=(self.pk,))


class Question(repository_model.BaseModel):
    # status
    HIGH = 'HIGH'
    HIGH_NORM = 'HIGH_NORM'
    NORM = 'NORM'
    LOW_NORM = 'LOW_NORM'
    LOW = 'LOW'
    DO_NOT_MATCH = 'DO_NOT_MATCH'

    ANSWER_CHOICE = [
        (HIGH, 'Высокая'),
        (HIGH_NORM, 'Выше среднего'),
        (NORM, 'Средняя'),
        (LOW_NORM, 'Ниже среднего'),
        (LOW, 'Низкая'),
        (DO_NOT_MATCH, 'Не соответствует'),
        # Fields

    ]

    title = models.CharField("Показатель", max_length=300)
    checklist = models.ForeignKey(CheckList, verbose_name="Чек-лист эеспертизы", on_delete=models.CASCADE)
    answer = models.CharField("Тип чек-листа", max_length=30, choices=ANSWER_CHOICE, blank=True)

    class Meta:
        verbose_name = u"Чек-лист экспертизы"
        verbose_name_plural = u"Чек-листы экспертиз"

    def __str__(self):
        return self.title

    # TODO: Поменять ПК

    def get_absolute_url(self):
        return reverse("inspections:inspections_CheckList_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("inspections:inspections_CheckList_update", args=(self.pk,))
