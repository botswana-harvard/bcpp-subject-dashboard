from django.conf import settings
from edc_base.utils import get_utcnow
from edc_base.view_mixins import EdcBaseViewMixin
from edc_constants.constants import MALE
from edc_dashboard.view_mixins import AppConfigViewMixin
from edc_dashboard.views import ListboardView
from edc_navbar import NavbarViewMixin
from household_dashboard.view_mixins import HouseholdQuerysetViewMixin
from plot_dashboard.view_mixins import PlotQuerysetViewMixin
from survey import SurveyViewMixin


class BaseListboardView(SurveyViewMixin, NavbarViewMixin, AppConfigViewMixin,
                        EdcBaseViewMixin, HouseholdQuerysetViewMixin, PlotQuerysetViewMixin,
                        ListboardView):

    app_config_name = 'bcpp_subject_dashboard'

    plot_queryset_lookups = [
        'household_member', 'household_structure', 'household', 'plot']
    household_queryset_lookups = [
        'household_member', 'household_structure', 'household']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(
            MALE=MALE,
            reference_datetime=get_utcnow())
        context.update(
            {k: v for k, v in self.url_names('anonymous_listboard_url_name')})
        return context
