from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.view_mixins import DashboardViewMixin as EdcDashboardViewMixin
from edc_navbar import NavbarViewMixin

from ....model_wrappers import AnonymousAppointmentModelWrapper
from ....model_wrappers import AnonymousConsentModelWrapper
from ....model_wrappers import AnonymousCrfModelWrapper
from ....model_wrappers import AnonymousRequisitionModelWrapper
from ....model_wrappers import AnonymousSubjectVisitModelWrapper
from .base_dashboard_view import BaseDashboardView


class DashboardView(
        BaseDashboardView, NavbarViewMixin, EdcDashboardViewMixin,
        AppConfigViewMixin, EdcBaseViewMixin,
        TemplateView):

    app_config_name = 'bcpp_subject_dashboard'

    navbar_name = 'anonymous'
    navbar_selected_item = 'anonymous'

    consent_model_wrapper_cls = AnonymousConsentModelWrapper
    consent_model = 'bcpp_subject.anonymousconsent'
    crf_model_wrapper_cls = AnonymousCrfModelWrapper
    requisition_model_wrapper_cls = AnonymousRequisitionModelWrapper
    visit_model_wrapper_cls = AnonymousSubjectVisitModelWrapper
    appointment_model_wrapper_cls = AnonymousAppointmentModelWrapper

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anonymous = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'anonymous': 'anonymous',
            'anonymous_dashboard_url_name': django_apps.get_app_config(
                'bcpp_subject_dashboard').anonymous_dashboard_url_name})
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
