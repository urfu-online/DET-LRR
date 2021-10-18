#  Уральский федеральный университет (c) 2021.
#  Цифровой университет/Цифровые образовательные технологии

import auto_prefetch
from django.db import models
from django.urls import reverse
from sortedm2m.fields import SortedManyToManyField

from lrr.repository.models import BaseModel


class ThematicPlan(BaseModel):
    digital_complex = models.ForeignKey("complexes.DigitalComplex", verbose_name="Цифровой Комплекс (ЭУМК)",
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
    thematic_plan = models.ForeignKey(ThematicPlan, related_name="themes", on_delete=models.CASCADE,
                                blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.complex}: {self.order} - {self.title}"


class Component(models.Model):
    thematic_plan = models.ForeignKey(ThematicPlan, on_delete=models.CASCADE, null=False)
    content = models.JSONField(verbose_name="Содержимое ячейки структурно-тематического плана", null=True, blank=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)
