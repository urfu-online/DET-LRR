from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from .models import User, Person, Student


@receiver(user_signed_up, sender=User)
def create_profile(*args, **kwargs):
    Person.objects.create(user=kwargs['user'])


@receiver(user_signed_up, sender=User)
def save_profile(*args, **kwargs):
    person = kwargs["user"].get_person()
    person.save()
