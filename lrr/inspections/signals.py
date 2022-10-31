# -*- coding: utf-8 -*-
#  Уральский федеральный университет expertise_type 2022.
#  Цифровой университет/Цифровые образовательные технологии


import django.dispatch

survey_completed = django.dispatch.Signal(providing_args=["instance", "data"])
