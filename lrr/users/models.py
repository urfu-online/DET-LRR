# -*- coding: utf-8 -*-
import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import MultipleObjectsReturned
from django.db import models as models
from django.db.models import CharField, Prefetch
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from lrr.repository.models import Source, DigitalResource, EduProgram


class User(AbstractUser):
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_person(self):
        person = Person.objects.filter(user=self)
        try:
            return person.first()
        except MultipleObjectsReturned:
            raise person

    @cached_property
    def get_groups(self):
        return self.groups.all().values_list('name', flat=True)

    def get_bookmarks(self):
        return self.bookmarkdigitalresource_set.all().prefetch_related(
            Prefetch('obj', queryset=DigitalResource.objects.prefetch_related("source_set", "copyright_holder", "owner",
                                                                              "language", "platform")
                     )
        )


class Person(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='person')

    location = models.CharField("Адрес проживания", max_length=150, null=True, blank=True)
    date_birthday = models.DateTimeField("Дата рождения", null=True, blank=True)
    city = models.CharField("Город", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    middle_name = models.CharField("Отчество", max_length=100, null=True, blank=True)
    country = models.CharField("Страна", max_length=100, null=True, blank=True)
    first_name = models.CharField("Имя", max_length=45, null=True, blank=True)
    avatar = models.ImageField("Изображение профиля", upload_to="upload/images/", null=True, blank=True)
    last_name = models.CharField("Фамилия", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "профиль"
        verbose_name_plural = "профили"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"

    @property
    def short_name(self):
        return f"{self.last_name} {self.first_name[0]}. {self.middle_name[0]}."

    def get_absolute_url(self):
        return reverse("repository_Person_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Person_update", args=(self.pk,))

    @classmethod
    def get_or_create(cls, user):
        try:
            obj = cls.objects.get(user=user)
        except cls.DoesNotExist:
            obj = cls(user=user)
            obj.save()

        return obj

    @classmethod
    def get_person(cls, user):
        try:
            obj = cls.objects.get(user=user)
        except cls.DoesNotExist:
            obj = None
        return obj


# TODO: add reciever

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)
#
# def person_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         person = Person.objects.create(user=instance)
#     else:
#         instance.person.save()
#
# post_save.connect(person_receiver, sender=settings.AUTH_USER_MODEL)


class Student(models.Model):
    person = models.ForeignKey("users.Person", on_delete=models.CASCADE)
    academic_group = models.ForeignKey("users.AcademicGroup", on_delete=models.PROTECT,
                                       verbose_name="Номер академической группы", null=True)

    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)

    class Meta:
        verbose_name = "студент"
        verbose_name_plural = "студенты"

    def __str__(self):
        return str(self.person)

    def get_absolute_url(self):
        return reverse("repository_Student_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Student_update", args=(self.pk,))

    @classmethod
    def get_academic_group_for_user(cls, user):
        try:
            obj = cls.objects.get(person__user=user)
        except cls.DoesNotExist:
            obj = None
        try:
            return obj.academic_group
        except:
            return None

    @classmethod
    def get_student(cls, user):
        try:
            obj = cls.objects.get(person__user=user)
        except cls.DoesNotExist:
            obj = None
        return obj


class AcademicGroup(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False, null=True)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False, null=True)
    number = models.CharField("Номер академической группы", max_length=30)
    eduprogram = models.ForeignKey("repository.EduProgram",
                                   verbose_name="Образовательная программа/Направление подготовки",
                                   related_name="eduprogram_academic_group",
                                   on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = "академическая группа"
        verbose_name_plural = "академические группы"

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("repository_AcademicGroup_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_AcademicGroup_update", args=(self.pk,))

    @classmethod
    def get_eduprogram_for_number(cls, number):
        try:
            obj = cls.objects.get(number=number)
        except cls.DoesNotExist:
            return None
        return obj.eduprogram


class ChoicesExpert(models.Model):
    # status
    METHODICAL = 'METHODICAL'
    CONTENT = 'CONTENT'
    TECH = 'TECH'

    STATUS_CHOICES = [
        (METHODICAL, 'Методическая'),
        (CONTENT, 'Содержательная'),
        (TECH, 'Техническая'),

    ]
    type = models.CharField("Вид экспертизы", max_length=30, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = "тип экспертизы"
        verbose_name_plural = "типы экспертиз"

    def __str__(self):
        return self.get_type_display()


class Expert(models.Model):
    person = models.ForeignKey("users.Person", on_delete=models.CASCADE, verbose_name="Пользователь")
    types = models.ManyToManyField('users.ChoicesExpert', verbose_name="Вид экспертизы", blank=True)
    subdivision = models.CharField('Подразделение/отрасль', max_length=500)

    class Meta:
        verbose_name = "эксперт"
        verbose_name_plural = "эксперты"

    def __str__(self):
        return str(self.person)

    def get_absolute_url(self):
        return reverse("users:expert_detail", args=(self.pk,))

    def get_user(self):
        return self.person.user

    @classmethod
    def get_expert(cls, user):
        try:
            obj = cls.objects.get(person__user=user)
        except cls.DoesNotExist:
            obj = None
        return obj


class GroupDisciplines(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    academic_group = models.ForeignKey("users.AcademicGroup", on_delete=models.CASCADE, verbose_name="Академическая группа",
                                       blank=True, null=True)
    subject = models.ForeignKey("repository.Subject", verbose_name="Дисциплина(ы)", on_delete=models.PROTECT,
                                blank=True, null=True)
    semestr = models.PositiveSmallIntegerField(verbose_name="Семестр", blank=True, null=True)

    class Meta:
        verbose_name = "дисциплина группы"
        verbose_name_plural = "дисциплины групп"

    def __str__(self):
        return f"{self.subject} - {self.semestr} семестр"
