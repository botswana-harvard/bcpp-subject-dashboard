from django.apps import apps as django_apps

from edc_appointment.constants import NEW_APPT
from edc_appointment.view_mixins import AppointmentViewMixin as BaseAppointmentMixin
from member.models import HouseholdMember

from ..wrappers import AppointmentModelWrapper


class AppointmentViewMixin(BaseAppointmentMixin):

    appointment_model_wrapper_cls = AppointmentModelWrapper
    appointment_model = 'bcpp_subject.appointment'

    @property
    def appointment_model_cls(self):
        return django_apps.get_model(self.appointment_model)

    @property
    def appointments(self):
        appointments = super().appointments
        for appointment in appointments:
            if appointment.appt_status == NEW_APPT:
                print(self.household_member, appointment)
                appointment.household_member = self.household_member
                appointment.save()
        return self.appointment_model_cls.objects.filter(
            household_member=self.household_member)

    def empty_appointment(self, **kwargs):
        household_member = HouseholdMember(
            household_structure=self.household_structure.object)
        return self.appointment_model_cls(household_member=household_member)
