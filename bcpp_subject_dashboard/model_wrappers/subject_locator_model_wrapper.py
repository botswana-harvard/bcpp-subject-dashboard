from django.apps import apps as django_apps
from edc_model_wrapper import ModelWrapper


class SubjectLocatorModelWrapper(ModelWrapper):
    model = 'bcpp_subject.subjectlocator'
    household_member_model = 'member.householdmember'
    admin_site_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').admin_site_name
    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').dashboard_url_name
    next_url_attrs = [
        'subject_identifier', 'household_identifier',
        'survey_schedule']

    @property
    def household_member_model_cls(self):
        return django_apps.get_model(self.household_member_model)

    @property
    def household_identifier(self):
        member = self.household_member_model_cls.objects.filter(
            subject_identifier=self.object.subject_identifier).first()
        return member.household_structure.household.household_identifier

    @property
    def survey_schedule(self):
        member = self.household_member_model_cls.objects.filter(
            subject_identifier=self.object.subject_identifier).last()
        return member.survey_schedule
