from django.apps import apps as django_apps
from edc_appointment.constants import NEW_APPT
from edc_appointment.view_mixins import AppointmentViewMixin as BaseAppointmentMixin

from ...model_wrappers import AppointmentModelWrapper


class AppointmentViewMixin(BaseAppointmentMixin):

    appointment_model_wrapper_cls = AppointmentModelWrapper
    household_member_model = 'member.householdmember'

    @property
    def appointment_model_cls(self):
        return self.appointment_model

    @property
    def appointments(self):
        appointments = super().appointments
        for appointment in appointments:
            if appointment.appt_status == NEW_APPT:
                appointment.household_member = self.household_member
                appointment.save()
        return self.appointment_model_cls.objects.filter(
            household_member=self.household_member)

    @property
    def household_member_model_cls(self):
        return django_apps.get_model(self.household_member_model)

    def empty_appointment(self, **kwargs):
        household_member = self.household_member_model_cls(
            household_structure=self.household_structure.object)
        return self.appointment_model_cls(household_member=household_member)
