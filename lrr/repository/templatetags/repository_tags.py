#  Уральский федеральный университет (c) 2021.
#  Цифровой университет/Цифровые образовательные технологии

from django import template

from ..models import BookmarkDigitalResource

register = template.Library()


@register.filter("favorited_by")
def favorited_by(resource, user):
    return BookmarkDigitalResource.objects.filter(obj=resource, user=user).exists()
