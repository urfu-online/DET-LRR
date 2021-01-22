# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404

from lrr.complexes import models as complex_model
from lrr.users.models import Person, Student

import logging
from django.views import generic


# import logging
#
logger = logging.getLogger(__name__)


def WorkPlanView(request):
    person = get_object_or_404(Person, user=request.user)
    academic_group = get_object_or_404(Student, person=Person.objects.get(user=request.user)).academic_group
    obj_plan = complex_model.WorkPlanAcademicGroup.objects.filter(academic_group=academic_group)
    return render(request, 'pages/work_plan_list.html',
                  {'academic_group': academic_group, 'obj_plan': obj_plan, 'person': person,  # 'status': status,
                   'DR': obj_plan[0].digital_resource.first()})
