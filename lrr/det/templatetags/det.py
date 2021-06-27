#  Уральский федеральный университет (c) 2021.
#  Цифровой университет/Цифровые образовательные технологии

from django import template
from django.conf import settings

register = template.Library()

DEFAULT_VERTICAL_ALIGN_RULE = {
    "body_va_class": "align-items-top",
    "get_container_class": "d-flex flex-row",

}

DEFAULT_VERTICAL_ALIGN_RULES = [
    {'LoginView': {"body_va_class": "align-items-center", "get_container_class": "d-flex flex-row"}},
    {'LogoutView': {"body_va_class": "align-items-top", "get_container_class": "wrapper d-flex flex-column"}},
]

VERTICAL_ALIGN_RULES = getattr(settings, 'VERTICAL_ALIGN_RULES', DEFAULT_VERTICAL_ALIGN_RULES)


@register.filter
def get_class(value, arg):
    rule = dict()
    for _rule in VERTICAL_ALIGN_RULES:
        rule = rule | _rule.get(value.__class__.__name__, dict())
    rule = DEFAULT_VERTICAL_ALIGN_RULE | rule
    return rule.get(arg, "")
