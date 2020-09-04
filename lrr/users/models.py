from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models as models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save


class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Person(models.Model):
    # Relationships
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                             related_name='person')

    # Fields
    location = models.CharField("Адрес проживания", max_length=150, null=True, blank=True)
    date_birthday = models.DateTimeField("Дата рождения", null=True, blank=True)
    city = models.CharField("Город", max_length=100, null=True, blank=True)
    created = models.DateTimeField("Создано", auto_now_add=True, editable=False)
    middle_name = models.CharField("Отчество", max_length=100)
    country = models.CharField("Страна", max_length=100, null=True, blank=True)
    first_name = models.CharField("Имя", max_length=45)
    avatar = models.ImageField("Изображение профиля", upload_to="upload/images/", null=True, blank=True)
    last_name = models.CharField("Фамилия", max_length=100)

    class Meta:
        verbose_name = u"Профиль"
        verbose_name_plural = u"Профили"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

    def get_absolute_url(self):
        return reverse("repository_Person_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Person_update", args=(self.pk,))

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
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("repository_Student_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_Student_update", args=(self.pk,))


class AcademicGroup(models.Model):
    number = models.CharField("Номер академической группы", max_length=30)

    class Meta:
        verbose_name = u"Академическая группа"
        verbose_name_plural = u"Академические группы"

    def __str__(self):
        return self.number

    def get_absolute_url(self):
        return reverse("repository_AcademicGroup_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("repository_AcademicGroup_update", args=(self.pk,))
