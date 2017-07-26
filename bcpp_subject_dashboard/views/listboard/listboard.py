import re

from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.utils.decorators import method_decorator

from ..wrappers import SubjectConsentModelWrapper
from .base_listboard import BaseListboardView


class ListboardView(BaseListboardView):

    label_lower = 'bcpp_subject.subjectconsent'
    model_wrapper_class = SubjectConsentModelWrapper

    @property
    def model(self):
        return django_apps.get_model(*self.label_lower.split('.'))

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset_filter_options(self, request, *args, **kwargs):
        options = super().get_queryset_filter_options(request, *args, **kwargs)
        if kwargs.get('subject_identifier'):
            options.update(
                {'subject_identifier': kwargs.get('subject_identifier')})
        if kwargs.get('survey_schedule'):
            options.update(
                {'survey_schedule': kwargs.get('survey_schedule')})
        return options

    def extra_search_options(self, search_term):
        q = Q()
        if re.match('^[A-Z]+$', search_term):
            q = Q(first_name__exact=search_term)
        return q
