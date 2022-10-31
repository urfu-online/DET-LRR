#  Уральский федеральный университет © 2021.
#  Цифровой университет/Цифровые образовательные технологии
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import logging

from django import template

register = template.Library()
logger = logging.getLogger(__name__)


@register.filter('user_in')
def user_in(objects, user):
    if user.is_authenticated:
        return objects.filter(user=user).exists()
    return False


@register.filter('has_group')
def has_group(user, group_name):
    """
    Проверяет, принадлежит ли этот пользователь к группе
    """
    if not user.is_authenticated:
        return False
    return group_name in user.get_groups


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Параметры URL в кодировке return, которые совпадают с параметрами текущего запроса,
    только с добавленными или измененными указанными параметрами GET.

    Он также удаляет все пустые параметры, чтобы все было в порядке,
    поэтому вы можете удалить параметр, установив для него значение `` "` `.

    Например, если вы находитесь на странице``/things/?with_frosting=true&page=5``,
    тогда

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    расширится до

    <a href="/things/?with_frosting=true&page=3">Page 3</a>

    Based on
    https://stackoverflow.com/questions/22734695/next-and-before-links-for-a-django-paginated-query/22735278#22735278
    """
    d = context['request'].GET.copy()
    for k, v in kwargs.items():
        d[k] = v
    for k in [k for k, v in d.items() if not v]:
        del d[k]
    return d.urlencode()
