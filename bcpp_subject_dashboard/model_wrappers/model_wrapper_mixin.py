from django.apps import apps as django_apps
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
