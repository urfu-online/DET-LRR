#  Уральский федеральный университет (c) 2021.
#  Цифровой университет/Цифровые образовательные технологии

from django.db import models
from django.urls import reverse
from sortedm2m.fields import SortedManyToManyField
import auto_prefetch
from lrr.repository.models import BaseModel


class Complex(auto_prefetch.Model):
    # thematic_plan = SortedManyToManyField("complexes.Theme")

    class Meta(auto_prefetch.Model.Meta):
        abstract = True


class Theme(models.Model):
    # content = models.ManyToManyField("complexes.Container")
    title = models.CharField(max_length=64, db_index=True)
    complex = models.ForeignKey("complexes.DigitalComplex", related_name="thematic_plan", on_delete=models.CASCADE,
                                blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.complex}: {self.order} - {self.title}"


class Cell(BaseModel):
    content = SortedManyToManyField("complexes.ComponentComplex")
    end_point = models.ForeignKey("complexes.Container", related_name="+", on_delete=models.SET_NULL, null=True)
    start_point = models.ForeignKey("complexes.Container", related_name="+", on_delete=models.SET_NULL, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class Container(BaseModel):
    TYPES = (
        ("theory", "Теория"),
        ("practice", "Практика")
    )
    type = models.CharField(max_length=30, choices=TYPES, default="theory")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)


class ThematicPlan(BaseModel):
    digital_complex = models.ForeignKey("complexes.DigitalComplex", verbose_name="Цифровой Комплекс (ЭУМК)",
                                        on_delete=models.CASCADE, null=True, blank=True)
    plan_object = models.JSONField(verbose_name="Объект плана", null=True, blank=True)

    class Meta:
        verbose_name = u"Структурно-тематический план"
        verbose_name_plural = u"Структурно-тематические планы"

    def __str__(self):
        return str(self.digital_complex)

    def get_themes(self):
        return self.digital_complex.get_themes()
