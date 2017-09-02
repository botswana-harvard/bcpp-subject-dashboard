from django.test import TestCase, tag
from edc_model_wrapper.tests import ModelWrapperTestHelper

from ..model_wrappers import AppointmentModelWrapper
from ..model_wrappers import RequisitionModelWrapper
from ..model_wrappers import SubjectConsentModelWrapper
from ..model_wrappers import SubjectLocatorModelWrapper
from ..model_wrappers import SubjectVisitModelWrapper
from .models import Appointment, SubjectVisit, HouseholdMember, HouseholdStructure, Household, Plot
from django.conf import settings


app_label = settings.APP_NAME


class MySubjectLocatorModelWrapper(SubjectLocatorModelWrapper):
    household_member_model = f'{app_label}.householdmember'


class TestModelWrappers(TestCase):

    model_wrapper_helper_cls = ModelWrapperTestHelper

    def setUp(self):
        self.subject_identifier = '066-111111111-1'
        self.survey_schedule = 'bcpp-survey.bcpp-year-3.community'
        self.survey = 'bcpp-survey.bcpp-year-3.ess.community'
        plot = Plot.objects.create(plot_identifier='111111-11')
        household = Household.objects.create(
            plot=plot,
            household_identifier='111111-11-11')
        household_structure = HouseholdStructure.objects.create(
            household=household,
            survey_schedule=self.survey_schedule)
        self.household_member = HouseholdMember.objects.create(
            household_structure=household_structure,
            subject_identifier=self.subject_identifier,
            age_in_years=25,
            survey_schedule=self.survey_schedule)

    @tag('1')
    def test_subject_consent(self):
        helper = self.model_wrapper_helper_cls(
            model_wrapper=SubjectConsentModelWrapper,
            app_label='bcpp_subject_dashboard',
            subject_identifier=self.subject_identifier,
            household_member=self.household_member,
            survey_schedule=self.survey_schedule)
        helper.test(self)

    @tag('1')
    def test_subject_locator(self):
        helper = self.model_wrapper_helper_cls(
            model_wrapper=MySubjectLocatorModelWrapper,
            app_label='bcpp_subject_dashboard',
            subject_identifier=self.subject_identifier)
        helper.test(self)

    @tag('1')
    def test_appointment(self):
        helper = self.model_wrapper_helper_cls(
            model_wrapper=AppointmentModelWrapper,
            app_label='bcpp_subject_dashboard',
            subject_identifier=self.subject_identifier,
            household_member=self.household_member,
            survey_schedule=self.survey_schedule,
            survey=self.survey)
        helper.test(self)

    @tag('1')
    def test_subject_visit(self):
        appointment = Appointment.objects.create(
            subject_identifier=self.subject_identifier,
            household_member=self.household_member,
            survey_schedule=self.survey_schedule,
            survey=self.survey)
        helper = self.model_wrapper_helper_cls(
            model_wrapper=SubjectVisitModelWrapper,
            app_label='bcpp_subject_dashboard',
            subject_identifier=self.subject_identifier,
            household_member=self.household_member,
            appointment=appointment,
            survey_schedule=self.survey_schedule,
            survey=self.survey)
        helper.test(self)

    @tag('1')
    def test_subject_requisition(self):
        appointment = Appointment.objects.create(
            subject_identifier=self.subject_identifier,
            household_member=self.household_member,
            survey_schedule=self.survey_schedule,
            survey=self.survey)
        subject_visit = SubjectVisit.objects.create(
            appointment=appointment,
            subject_identifier=self.subject_identifier,
            household_member=self.household_member,
            survey_schedule=self.survey_schedule,
            survey=self.survey)
        helper = self.model_wrapper_helper_cls(
            model_wrapper=RequisitionModelWrapper,
            app_label='bcpp_subject_dashboard',
            subject_visit=subject_visit,
            survey_schedule=self.survey_schedule,
            survey=self.survey)
        helper.test(self)
