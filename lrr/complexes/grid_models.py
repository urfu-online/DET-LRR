#  Уральский федеральный университет (c) 2021.
#  Цифровой университет/Цифровые образовательные технологии

from django.db import models
from django.urls import reverse
from sortedm2m.fields import SortedManyToManyField

from lrr.repository.models import BaseModel


class Complex(models.Model):
    # thematic_plan = SortedManyToManyField("complexes.Theme")

    class Meta:
        abstract = True


class Theme(models.Model):
    content = models.ManyToManyField("complexes.Container")
    title = models.CharField(max_length=64, db_index=True)
    complex = models.ForeignKey("complexes.DigitalComplex", related_name="thematic_plan", on_delete=models.CASCADE, blank=True, null=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("complexes_Theme_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("complexes_Theme_update", args=(self.pk,))


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


