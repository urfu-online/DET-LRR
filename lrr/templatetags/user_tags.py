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


@register.inclusion_tag("repository/dr_cards.html")
def get_resources(res, *args, **kwargs):
    subject = kwargs.get('subject', None)
    edu_program = kwargs.get('edu_program', None)
    if subject and edu_program:
        return {'objects': res.get_recommended_resources_by_subject(subject, edu_program)}
    elif subject and not edu_program:
        return {'objects': res.get_resources_by_subject(subject)}


@register.filter('has_owner_resource')
def has_owner_resource(user, res):
    owner = res.get_owner(user)
    return owner


@register.filter('has_owner_complex')
def has_owner_complex(user, complex):
    owner = complex.get_owner(user)
    return owner


@register.filter('has_group')
def has_group(user, group_name):
    """
    Verifica se este usuário pertence a um grupo
    """
    try:
        groups = user.groups.all().values_list('name', flat=True)
        return True if group_name in groups else False
    except:
        return None


@register.filter('in_tag')
def in_tag(things, category):
    return things.filter(tag=category)


@register.simple_tag(takes_context=True)
def param_replace(context, **kwargs):
    """
    Return encoded URL parameters that are the same as the current
    request's parameters, only with the specified GET parameters added or changed.

    It also removes any empty parameters to keep things neat,
    so you can remove a parm by setting it to ``""``.

    For example, if you're on the page ``/things/?with_frosting=true&page=5``,
    then

    <a href="/things/?{% param_replace page=3 %}">Page 3</a>

    would expand to

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
