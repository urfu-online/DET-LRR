#  Уральский федеральный университет (c) 2022.
#  Цифровой университет/Цифровые образовательные технологии
from functools import wraps

from django.shortcuts import get_object_or_404

from lrr.inspections.models import ExpertiseOpinion, ExpertiseType


def expertise_available(func):
    """
    Checks if a survey is available (published and not expired). Use this as a decorator for view functions.
    """

    @wraps(func)
    def expertise_check(self, request, *args, **kwargs):
        expertise_type = get_object_or_404(
            ExpertiseType.objects.prefetch_related("questions", "questions__category"), id=kwargs["id"]
        )
        expertise_opinion = get_object_or_404(ExpertiseOpinion, pk=kwargs["expertise_opinion_pk"])
        return func(self, request, *args, **kwargs, expertise_type=expertise_type, expertise_opinion=expertise_opinion)

    return expertise_check
