from django.apps import apps as django_apps

from .crf_model_wrapper import CrfModelWrapper as Base


class AnonymousCrfModelWrapper(Base):

    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').anonymous_dashboard_url_name
