from django.apps import apps as django_apps

from .appointment_model_wrapper import AppointmentModelWrapper as Base
from .subject_visit_model_wrapper import SubjectVisitModelWrapper


class AnonymousAppointmentModelWrapper(Base):
    dashboard_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').anonymous_dashboard_url_name
    visit_model_wrapper_cls = SubjectVisitModelWrapper
    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').anonymous_dashboard_url_name
