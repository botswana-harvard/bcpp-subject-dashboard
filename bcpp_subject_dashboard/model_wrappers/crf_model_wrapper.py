from django.apps import apps as django_apps
from edc_model_wrapper import ModelWrapper


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
