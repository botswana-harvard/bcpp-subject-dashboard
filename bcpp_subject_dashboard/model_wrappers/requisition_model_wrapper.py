from django.apps import apps as django_apps
from edc_model_wrapper import ModelWrapper


class RequisitionModelWrapper(ModelWrapper):

    model = 'bcpp_subject.subjectrequisition'
    requisition_panel_name = None
    admin_site_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').admin_site_name
    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').dashboard_url_name
    next_url_attrs = [
        'appointment', 'household_identifier', 'subject_identifier',
        'survey_schedule', 'survey']
    querystring_attrs = ['subject_visit', 'panel_name']

    @property
    def panel_name(self):
        return self.requisition_panel_name

    @property
    def subject_identifier(self):
        return str(self.object.subject_visit.subject_identifier)

    @property
    def subject_visit(self):
        return self.object.subject_visit.id

    @property
    def appointment(self):
        return str(self.object.subject_visit.appointment.id)

    @property
    def household_identifier(self):
        return (self.object.subject_visit.household_member
                .household_structure
                .household
                .household_identifier)

    @property
    def survey(self):
        return self.object.survey

    @property
    def survey_schedule(self):
        return self.object.survey_schedule

#     @property
#     def survey_object(self):
#         return self.subject_visit.survey_object

#     @property
#     def survey_schedule_object(self):
#         return self.subject_visit.survey_schedule_object
