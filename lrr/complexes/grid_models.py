#  Уральский федеральный университет (c) 2021.
#  Цифровой университет/Цифровые образовательные технологии

import auto_prefetch
from django.contrib.postgres.fields import IntegerRangeField
from django.db import models

from lrr.repository.models import BaseModel


class ThematicPlan(BaseModel):
    digital_complex = auto_prefetch.ForeignKey("complexes.DigitalComplex",
                                               verbose_name="Цифровой Комплекс (ЭУМК)",
                                               related_name="thematic_plan", on_delete=models.CASCADE)
    plan_object = models.JSONField(verbose_name="Объект плана", null=True, blank=True)

    class Meta:
        verbose_name = "Структурно-тематический план"
        verbose_name_plural = "Структурно-тематические планы"

    def __str__(self):
        return str(self.digital_complex)

    def get_themes(self):
        return self.digital_complex.get_themes()


class Theme(models.Model):
    title = models.CharField(max_length=64, db_index=True)
    thematic_plan = auto_prefetch.ForeignKey(ThematicPlan, related_name="themes",
                                             on_delete=models.CASCADE,
                                             blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name = "тема"
        verbose_name_plural = "темы структурно-тематического плана"

    def __str__(self):
        return f"{self.thematic_plan.digital_complex}: {self.order} - {self.title}"


class PlanComponent(models.Model):
    ASYNC = 'ASYNC'
    SYNC = 'SYNC'
    UNKNOWN = 'UNKNOWN'

    CELL_TYPE = [
        (UNKNOWN, 'не определено'),
        (ASYNC, 'асинхронные мероприятия'),
        (SYNC, 'синхронные мероприятия'),
    ]

    thematic_plan = models.ForeignKey(ThematicPlan, on_delete=models.CASCADE, null=False)
    type = models.CharField("Тип", max_length=7, choices=CELL_TYPE, null=True)
    methodology_description = models.CharField("Методологическое описание", max_length=1024, blank=True, null=True)
    content = models.JSONField(verbose_name="Содержимое ячейки структурно-тематического плана", null=True, blank=True)
    week_range = IntegerRangeField("Диапазон", blank=True, null=True)

    class Meta:
        verbose_name = "компонент"
        verbose_name_plural = "компоненты структурно-тематического плана"

    def __str__(self):
        return str(self.pk)
