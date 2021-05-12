#  Уральский федеральный университет (c) 2021.
#  Цифровой университет/Цифровые образовательные технологии

import logging

import data_wizard
from rest_framework import serializers
from rest_framework.fields import ListField, DictField

from .models import Indicator

logger = logging.getLogger(__name__)


class StringArrayField(ListField):
    """
    String representation of an array field.
    """

    def to_representation(self, obj):
        obj = super().to_representation(self, obj)
        return ";".join([str(element) for element in obj])

    def to_internal_value(self, data, *args, **kwargs):
        if ";" in data:
            return data.split(";")
        return "{}"


class RangeField(DictField):
    def to_representation(self, obj):
        obj = super().to_representation(self, obj)
        return f"{obj['lower']}:{obj['upper']}"

    def to_internal_value(self, data, *args, **kwargs):
        if ":" in data:
            return f"[{data.split(':')[0]}, {data.split(':')[1]})"
        return None


class IndicatorSerializer(serializers.ModelSerializer):
    values = StringArrayField(allow_empty=True, allow_null=True)
    num_values = RangeField(allow_empty=True, allow_null=True)

    class Meta:
        model = Indicator
        fields = '__all__'

        # Optional - see options below
        data_wizard = {
            'header_row': 0,
            'start_row': 1,
            'show_in_list': True,
            'idmap': data_wizard.idmap.existing,
        }


data_wizard.register("Показатели экспертизы", IndicatorSerializer)
