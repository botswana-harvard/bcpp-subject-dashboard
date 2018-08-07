from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ...model_wrappers import AnonymousConsentModelWrapper
from .base_listboard import BaseListboardView


class AnonymousListboardView(BaseListboardView):

    model = 'bcpp_subject.anonymousconsent'
    model_wrapper_cls = AnonymousConsentModelWrapper
    listboard_url_name = django_apps.get_app_config(
        'bcpp_subject_dashboard').anonymous_listboard_url_name
    paginate_by = 10

    navbar_name = 'anonymous'
    navbar_selected_item = 'anonymous_subject'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
