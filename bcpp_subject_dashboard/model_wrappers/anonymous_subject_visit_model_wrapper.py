from django.apps import apps as django_apps

from .subject_visit_model_wrapper import SubjectVisitModelWrapper as Base


class AnonymousSubjectVisitModelWrapper(Base):

    next_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').anonymous_dashboard_url_name
