#  Уральский федеральный университет © 2022.
#  Цифровой университет/Цифровые образовательные технологии
from functools import wraps

from django.shortcuts import get_object_or_404

from lrr.inspections.models import ExpertiseOpinion, ExpertiseType, ExpertiseRequest


def expertise_available(func):
    """
    Checks if expertise is available (published and not expired). Use this as a decorator for view functions.
    """

    @wraps(func)
    def expertise_check(self, request, *args, **kwargs):
        expertise_opinion = get_object_or_404(
            ExpertiseOpinion, pk=kwargs["pk"]
        )
        return func(self, request, *args, **kwargs, expertise_opinion=expertise_opinion)

    return expertise_check
