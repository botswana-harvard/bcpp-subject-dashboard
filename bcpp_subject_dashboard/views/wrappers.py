from django.apps import apps as django_apps
from django.core.exceptions import ObjectDoesNotExist
from django.urls.base import reverse

from edc_appointment.views import AppointmentModelWrapper
from edc_model_wrapper import ModelWrapper


class ModelWrapperMixin(ModelWrapper):

    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').dashboard_url_name
    next_url_attrs = [
        'household_identifier', 'subject_identifier', 'survey_schedule', 'survey']
    querystring_attrs = {}

    def add_extra_attributes_after(self):
        super().add_extra_attributes_after()
        self.survey = self.object.survey
        self.survey_schedule = self.object.survey_schedule

    @property
    def survey_object(self):
        return self.object.survey_object

    @property
    def survey_schedule_object(self):
        return self.object.survey_schedule_object

    @property
    def members(self):
        return (self.object
                .household_member
                .household_structure
                .householdmember_set.all())

    @property
    def plot_identifier(self):
        return (self.object
                .household_member
                .household_structure
                .household
                .plot
                .plot_identifier)

    @property
    def household_identifier(self):
        return (self.object
                .household_member
                .household_structure
                .household
                .household_identifier)

    @property
    def community_name(self):
        return self.object.survey_schedule_object.map_area_display


class SubjectVisitModelWrapper(ModelWrapperMixin):

    model = 'bcpp_subject.subjectvisit'
    next_url_attrs = [
        'appointment', 'household_identifier', 'subject_identifier',
        'survey_schedule', 'survey']
    querystring_attrs = ['household_member']

    @property
    def household_member(self):
        return self.object.household_member.id


class AppointmentModelWrapper(AppointmentModelWrapper, ModelWrapperMixin):

    model = 'bcpp_subject.appointment'
    visit_model_wrapper_cls = SubjectVisitModelWrapper
    dashboard_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').dashboard_url_name

    @property
    def household_member(self):
        return self.object.household_member.id

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


class CrfModelWrapper(ModelWrapper):

    admin_site_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').admin_site_name
    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').dashboard_url_name
    next_url_attrs = [
        'appointment', 'household_identifier', 'subject_identifier',
        'survey_schedule', 'survey']
    querystring_attrs = ['subject_visit']

    @property
    def appointment(self):
        return self.object.subject_visit.appointment

    @property
    def subject_visit(self):
        return self.object.subject_visit

    @property
    def household_member(self):
        return self.object.subject_visit.household_member

    @property
    def survey(self):
        return self.object.subject_visit.survey

    @property
    def survey_schedule(self):
        return self.object.subject_visit.survey_schedule

    @property
    def survey_object(self):
        return self.object.subject_visit.survey_object

    @property
    def survey_schedule_object(self):
        return self.object.subject_visit.survey_schedule_object

    @property
    def household_identifier(self):
        return (self.object
                .subject_visit
                .household_member
                .household_structure
                .household
                .household_identifier)


class SubjectLocatorModelWrapper(ModelWrapper):
    model = 'bcpp_subject.subjectlocator'
    admin_site_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').admin_site_name
    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').dashboard_url_name
    next_url_attrs = [
        'subject_identifier', 'household_identifier',
        'survey_schedule']


class RequisitionModelWrapper(ModelWrapper):

    admin_site_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').admin_site_name
    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').dashboard_url_name
    next_url_attrs = [
        'appointment', 'household_identifier', 'subject_identifier',
        'survey_schedule', 'survey']
    querystring_attrs = ['subject_visit', 'panel_name']

    @property
    def subject_visit(self):
        return self.object.subject_visit

    @property
    def appointment(self):
        return self.object.subject_visit.appointment

    @property
    def household_member(self):
        return self.subject_visit.household_member

    @property
    def survey(self):
        return self.subject_visit.survey

    @property
    def survey_schedule(self):
        return self.subject_visit.survey_schedule

    @property
    def survey_object(self):
        return self.subject_visit.survey_object

    @property
    def survey_schedule_object(self):
        return self.subject_visit.survey_schedule_object

    @property
    def household_identifier(self):
        return (self.household_member
                .household_structure
                .household
                .household_identifier)


class SubjectConsentModelWrapper(ModelWrapper):

    model = 'bcpp_subject.subjectconsent'
    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').dashboard_url_name
    next_url_attrs = [
        'household_identifier', 'subject_identifier', 'survey_schedule']
    querystring_attrs = [
        'gender', 'household_member', 'first_name', 'initials']

    @property
    def household_member(self):
        return str(self.object.household_member.id)

    @property
    def household_identifier(self):
        return (self.object.household_member.
                household_structure.household.household_identifier)

    @property
    def plot_identifier(self):
        return (self.object.household_member.
                household_structure.household.plot.plot_identifier)

    @property
    def first_name(self):
        return self.object.household_member.first_name

    @property
    def gender(self):
        return self.object.household_member.gender

    @property
    def members(self):
        return (self.object.household_member.
                household_structure.householdmember_set.all().
                order_by('first_name'))


class AnonymousConsentModelWrapper(ModelWrapper):

    model = 'bcpp_subject.anonymousconsent'
    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').anonymous_dashboard_url_name
    next_url_attrs = [
        'household_identifier', 'subject_identifier', 'survey_schedule']
    querystring_attrs = [
        'gender', 'household_member', 'first_name', 'initials']

    @property
    def household_member(self):
        return str(self.object.household_member.id)

    @property
    def household_identifier(self):
        return (self.object.household_member.
                household_structure.household.household_identifier)

    @property
    def first_name(self):
        return 'anonymous'

    @property
    def gender(self):
        return self.object.household_member.gender
