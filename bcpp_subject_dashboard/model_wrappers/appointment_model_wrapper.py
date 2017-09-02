from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from django.urls.base import reverse
from edc_appointment.views import AppointmentModelWrapper

from .model_wrapper_mixin import ModelWrapperMixin
from .subject_visit_model_wrapper import SubjectVisitModelWrapper


class AppointmentModelWrapper(AppointmentModelWrapper, ModelWrapperMixin):

    model = 'bcpp_subject.appointment'
    visit_model_wrapper_cls = SubjectVisitModelWrapper
    dashboard_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').dashboard_url_name

    @property
    def household_member(self):
        return str(self.object.household_member.id)

    @property
    def wrapped_visit(self):
        """Returns a wrapped persistent or non-persistent visit
        instance.
        """
        # FIXME: to much overriden from super class
        # only difference are the options for the visit model
        try:
            return self.visit_model_wrapper_cls(self.object.subjectvisit)
        except ObjectDoesNotExist:
            visit_model = django_apps.get_model(
                *self.visit_model_wrapper_cls.model.split('.'))
            return self.visit_model_wrapper_cls(
                visit_model(
                    household_member=self.object.household_member,
                    appointment=self.object,
                    subject_identifier=self.subject_identifier,
                    survey_schedule=self.survey_schedule_object.field_value,
                    survey=self.survey_object.field_value))

    @property
    def forms_url(self):
        """Returns a reversed URL to show forms for this
        appointment/visit.

        This is standard for edc_dashboard
        """
        # FIXME: to much overriden from super class
        # only difference are the extra kwargs tp reverse
        kwargs = dict(
            subject_identifier=self.subject_identifier,
            appointment=self.object.id,
            household_identifier=self.household_identifier,
            survey=self.survey_object.field_value,
            survey_schedule=self.survey_schedule_object.field_value)
        return reverse(self.dashboard_url_name, kwargs=kwargs)
