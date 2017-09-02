from django.apps import apps as django_apps
from edc_model_wrapper import ModelWrapper


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
