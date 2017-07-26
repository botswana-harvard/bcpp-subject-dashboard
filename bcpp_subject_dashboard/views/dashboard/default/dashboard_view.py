from django.apps import apps as django_apps
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from edc_base.view_mixins import EdcBaseViewMixin
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.view_mixins import DashboardViewMixin as EdcDashboardViewMixin

from ...wrappers import CrfModelWrapper, RequisitionModelWrapper
from ...wrappers import SubjectVisitModelWrapper, SubjectConsentModelWrapper
from .base_dashboard_view import BaseDashboardView


class DashboardView(
        BaseDashboardView, EdcDashboardViewMixin,
        AppConfigViewMixin, EdcBaseViewMixin,
        TemplateView):

    app_config_name = 'bcpp_subject_dashboard'
    navbar_item_selected = 'bcpp_subject'
    consent_model_wrapper_cls = SubjectConsentModelWrapper
    consent_model = 'bcpp_subject.subjectconsent'
    offstudy_model = 'bcpp_subject.subjectoffstudy'
    crf_model_wrapper_cls = CrfModelWrapper
    requisition_model_wrapper_cls = RequisitionModelWrapper
    visit_model_wrapper_cls = SubjectVisitModelWrapper

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.anonymous = None

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        SubjectOffstudy = django_apps.get_model(self.offstudy_model)
        try:
            subject_offstudy = SubjectOffstudy.objects.get(
                subject_identifier=self.subject_identifier)
        except SubjectOffstudy.DoesNotExist:
            subject_offstudy = None
        context.update(
            subject_offstudy=subject_offstudy,
            anonymous=None)
        return context
