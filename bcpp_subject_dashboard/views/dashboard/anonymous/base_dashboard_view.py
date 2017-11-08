from bcpp_referral.referral_view_mixin import ReferralViewMixin
from edc_subject_dashboard.view_mixins import SubjectVisitViewMixin, ShowHideViewMixin, SubjectIdentifierViewMixin
from edc_metadata.view_mixins import MetaDataViewMixin
from household_dashboard.view_mixins import HouseholdLogEntryViewMixin
from household_dashboard.view_mixins import HouseholdViewMixin, HouseholdStructureViewMixin
from member_dashboard.view_mixins import HouseholdMemberViewMixin
from survey.view_mixins import SurveyViewMixin

from ..appointment_view_mixin import AppointmentViewMixin
from ..consent_view_mixin import ConsentViewMixin
from ..visit_schedule_view_mixin import VisitScheduleViewMixin
from ....views.dashboard.status_helper_view_mixin import StatusHelperViewMixin


class BaseDashboardView(
        ReferralViewMixin,
        StatusHelperViewMixin,
        MetaDataViewMixin,
        ConsentViewMixin,
        SubjectVisitViewMixin,
        AppointmentViewMixin,
        VisitScheduleViewMixin,
        HouseholdMemberViewMixin,
        HouseholdLogEntryViewMixin,
        HouseholdStructureViewMixin,
        HouseholdViewMixin,
        SurveyViewMixin,
        ShowHideViewMixin,
        SubjectIdentifierViewMixin):
    pass
