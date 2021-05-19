# -*- coding: utf-8 -*-
import uuid
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import IntegerRangeField
from django.core.exceptions import MultipleObjectsReturned
from django.db import models as models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


# from lrr.repository.models import Direction


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def get_person(self):
        person = Person.objects.filter(user=self)
        try:
            return person.first()
        except MultipleObjectsReturned:
            raise person


class Person(models.Model):
    # Relationships
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='person')

    # Fields
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
        verbose_name = u"Профиль"
        verbose_name_plural = u"Профили"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

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
    # Relationships
    person = models.ForeignKey("users.Person", on_delete=models.CASCADE)
    academic_group = models.ForeignKey("users.AcademicGroup", on_delete=models.PROTECT,
                                       verbose_name="Номер академической группы")

    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)

    class Meta:
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенты"

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
        return obj.academic_group

    @classmethod
    def get_student(cls, user):
        try:
            obj = cls.objects.get(person__user=user)
        except cls.DoesNotExist:
            obj = None
        return obj


class AcademicGroup(models.Model):
    number = models.CharField("Номер академической группы", max_length=30)
    eduprogram = models.ForeignKey("repository.EduProgram",
                                   verbose_name="Образовательная программа/Направление подготовки",
                                   related_name="eduprogram_academic_group",
                                   on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = u"Академическая группа"
        verbose_name_plural = u"Академические группы"

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
            obj = None
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
        # Fields

    ]
    type = models.CharField("Вид экспертизы", max_length=30, choices=STATUS_CHOICES)

    class Meta:
        verbose_name = u"Тип экспертизы"
        verbose_name_plural = u"Типы экспертиз"

    def __str__(self):
        return self.get_type_display()


class Expert(models.Model):
    person = models.ForeignKey("users.Person", on_delete=models.CASCADE, verbose_name="Пользователь")
    types = models.ManyToManyField('users.ChoicesExpert', verbose_name="Вид экспертизы", blank=True)
    subdivision = models.CharField('Подразделение/отрасль', max_length=500)

    class Meta:
        verbose_name = u"Эксперт"
        verbose_name_plural = u"Эксперты"

    def __str__(self):
        return str(self.person)

    def get_absolute_url(self):
        return reverse("users:expert_detail", args=(self.pk,))

    @classmethod
    def get_expert(cls, user):
        try:
            obj = cls.objects.get(person__user=user)
        except cls.DoesNotExist:
            obj = None
        return obj

    # def get_update_url(self):
    #     return reverse("", args=(self.pk,))


class GroupDisciplines(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    last_updated = models.DateTimeField("Последние обновление", auto_now=True, editable=False)

    group = models.ForeignKey("users.AcademicGroup", on_delete=models.CASCADE, verbose_name="Академическая группа",
                              blank=True)
    subjects = models.ManyToManyField("repository.Subject", verbose_name="Дисциплина(ы)", blank=True)
    semestr = models.PositiveSmallIntegerField(verbose_name="Семестр", blank=True, null=True)

    class Meta:
        verbose_name = u"Дисциплина группы"
        verbose_name_plural = u"Дисциплины групп"

    def __str__(self):
        return f"{self.group}/{self.subjects}"
