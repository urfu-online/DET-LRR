from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from .models import User, Person, Student


@receiver(user_signed_up, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Person.objects.create(user=instance)


@receiver(user_signed_up, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.person.save()
