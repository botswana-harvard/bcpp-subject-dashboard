from django.apps import apps as django_apps
from edc_model_wrapper import ModelWrapper


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
    def correct_consent(self):
        """Returns a correct consent.
        """
        from bcpp_subject.models import CorrectConsent
        from correct_consent.correct_consent_model_wrapper import CorrectConsentModelWrapper
        try:
            correct_consent = CorrectConsent.objects.get(subject_consent=self.object)
        except CorrectConsent.DoesNotExist:
            correct_consent = CorrectConsent(subject_consent=self.object)
        if correct_consent:
            correct_consent = CorrectConsentModelWrapper(correct_consent)
        return correct_consent

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
