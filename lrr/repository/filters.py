import django_filters
from . import models


class DigitalResourceFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = models.DigitalResource
        fields = ['title', 'platform', 'keywords']
