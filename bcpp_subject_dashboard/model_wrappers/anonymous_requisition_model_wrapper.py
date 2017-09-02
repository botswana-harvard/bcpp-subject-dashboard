from django.apps import apps as django_apps

from .requisition_model_wrapper import RequisitionModelWrapper as Base


class AnonymousRequisitionModelWrapper(Base):

    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').anonymous_dashboard_url_name
