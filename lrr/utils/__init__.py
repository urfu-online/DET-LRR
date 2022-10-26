from typing import Any

from django.utils.text import slugify


def slugify(obj: Any) -> str:
    return slugify(str(obj), allow_unicode=True)
