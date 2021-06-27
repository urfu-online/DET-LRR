# -*- coding: utf-8 -*-
import logging

from django.conf import settings
from django.shortcuts import redirect, render, reverse
from django.utils import timezone
from django.views.generic import View

from lrr.survey.decorators import survey_available
from lrr.survey.forms import ResponseForm

LOGGER = logging.getLogger(__name__)


class SurveyDetail(View):
    @survey_available
    def get(self, request, *args, **kwargs):
        survey = kwargs.get("survey")
        step = kwargs.get("step", 0)
        expertise_request = kwargs.get("expertise_request")
        expertise_request_pk = kwargs.get("expertise_request_pk")
        # expert = Expert.get_expert(user=request.user)
        if survey.template is not None and len(survey.template) > 4:
            template_name = survey.template
        else:
            if survey.is_all_in_one_page():
                template_name = "survey/one_page_survey.html"
            else:
                template_name = "survey/survey.html"
        if survey.need_logged_user and not request.user.is_authenticated:
            return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))

        form = ResponseForm(survey=survey, user=request.user, step=step, expertise_request=expertise_request)
        categories = form.current_categories()

        asset_context = {
            # If any of the widgets of the current form has a "date" class, flatpickr will be loaded into the template
            "flatpickr": any([field.widget.attrs.get("class") == "date" for _, field in form.fields.items()])
        }
        context = {
            "response_form": form,
            "survey": survey,
            "categories": categories,
            "step": step,
            "asset_context": asset_context,
            "expertise_request": expertise_request,
            "expertise_request_pk": expertise_request_pk,
        }

        return render(request, template_name, context)

    @survey_available
    def post(self, request, *args, **kwargs):
        survey = kwargs.get("survey")
        expertise_request = kwargs.get("expertise_request")
        expertise_request_pk = kwargs.get("expertise_request_pk")
        if survey.need_logged_user and not request.user.is_authenticated:
            return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))

        form = ResponseForm(request.POST, survey=survey, user=request.user, step=kwargs.get("step", 0),
                            expertise_request=expertise_request)
        categories = form.current_categories()

        # if not survey.editable_answers and form.response is not None:
        #     LOGGER.info("Redirects to survey list after trying to edit non editable answer.")
        #     return redirect(reverse("survey:survey-list"))
        context = {
            "response_form": form,
            "survey": survey,
            "categories": categories,
            "expertise_request": expertise_request,
            "expertise_request_pk": expertise_request_pk
        }
        if form.is_valid():
            expertise_request.date = timezone.now()
            expertise_request.status = 'END'
            expertise_request.save()
            return self.treat_valid_form(form, kwargs, request, survey, expertise_request)
        return self.handle_invalid_form(context, form, request, survey)

    @staticmethod
    def handle_invalid_form(context, form, request, survey):
        LOGGER.info("Non valid form: <%s>", form)
        if survey.template is not None and len(survey.template) > 4:
            template_name = survey.template
        else:
            if survey.is_all_in_one_page():
                template_name = "survey/one_page_survey.html"
            else:
                template_name = "survey/survey.html"
        return render(request, template_name, context)

    def checking_answers(self, kwargs, request, survey, expertise_request):
        pass  # TODO: статус экспертизы

    def treat_valid_form(self, form, kwargs, request, survey, expertise_request):
        session_key = "survey_%s" % (kwargs["id"],)
        if session_key not in request.session:
            request.session[session_key] = {}
        for key, value in list(form.cleaned_data.items()):
            request.session[session_key][key] = value
            request.session.modified = True
        next_url = form.next_step_url()
        response = None
        if survey.is_all_in_one_page():
            response = form.save()
        else:
            # when it's the last step
            if not form.has_next_step():
                save_form = ResponseForm(request.session[session_key], survey=survey, user=request.user,
                                         expertise_request=expertise_request)
                if save_form.is_valid():
                    response = save_form.save()
                else:
                    LOGGER.warning("A step of the multipage form failed but should have been discovered before.")
        # if there is a next step
        if next_url is not None:
            return redirect(next_url)
        del request.session[session_key]
        if response is None:
            return redirect(reverse("inspections:expertise_completion"))
        next_ = request.session.get("next", None)
        if next_ is not None:
            if "next" in request.session:
                del request.session["next"]
            return redirect(next_)
        return redirect("inspections:expertise_completion", uuid=expertise_request.pk)
