from django.apps import apps as django_apps
from edc_consent.view_mixins import ConsentViewMixin as BaseConsentViewMixin
from edc_base.utils import get_uuid


class ConsentViewMixin(BaseConsentViewMixin):

    @property
    def empty_consent(self):
        """Returns a new unsaved mock consent model.
        """
        consent_model = django_apps.get_model(*self.consent_model.split('.'))
        return consent_model(
            consent_identifier=get_uuid(),
            household_member=self.household_member,
            survey_schedule=self.household_member.survey_schedule_object.field_value,
            version=self.consent_object.version)
