from django.apps import apps as django_apps
from django.test import TestCase
from django.test.client import RequestFactory
from django.views.generic.base import ContextMixin
from django.test.utils import override_settings

#
# class TestView(EdcDeviceViewMixin, ContextMixin):
#     pass


class TestHomeView(TestCase):

    def setUp(self):
        pass
#         self.view = HomeView()
#         self.view.request = RequestFactory()
#         self.view.request.META = {'HTTP_CLIENT_IP': '1.1.1.1'}
#
#     def test_context(self):
#         context = self.view.get_context_data()
#         self.assertIn('project_name', context)
#         self.assertIn('device_id', context)
#         self.assertIn('device_role', context)
#         self.assertIn('ip_address', context)


class TestViewMixin(TestCase):

    def setUp(self):
        pass
#         self.view = TestView()
#         self.view.request = RequestFactory()
#         self.view.request.META = {'HTTP_CLIENT_IP': '1.1.1.1'}

#     def test_context(self):
#         context = self.view.get_context_data()
#         self.assertIn('device_id', context)
#         self.assertIn('device_role', context)
#         self.assertIn('ip_address', context)
#
#     def test_context_with_values(self):
#         with override_settings(DEVICE_ID='10', DEVICE_ROLE=CLIENT):
#             app_config = django_apps.get_app_config('edc_device')
#             app_config.device_id = None
#             app_config.device_role = None
#             app_config.ready()
#             context = self.view.get_context_data()
#             self.assertEqual(context.get('device_id'), '10')
#             self.assertEqual(context.get('device_role'), CLIENT)
#
#     def test_context_ip(self):
#         context = self.view.get_context_data()
#         self.assertEqual(context.get('ip_address'), '1.1.1.1')
#
#     def test_context_ip_missing_meta(self):
#         del self.view.request.META
#         context = self.view.get_context_data()
#         self.assertEqual(context.get('ip_address'), None)
# from django.test import TestCase, tag
#
# from django.views.generic.base import TemplateView
# from django.test.client import RequestFactory
#
# # from ..models import SubjectConsent
# # from ..views import DashboardView
# # from ..views.dashboard_view import BcppDashboardExtraFieldMixin
# #
# # from .test_mixins import SubjectMixin
#
#
# @tag('me2')
# class TestDashboard(SubjectMixin, TestCase):
#
#     def setUp(self):
#         super().setUp()
#         self.visit = self.make_subject_visit_for_consented_subject(
#             'T0', report_datetime=self.get_utcnow())
#         self.appointment = self.visit.appointment
#         self.subject_identifier = self.appointment.subject_identifier
#         self.subject_consent = (
#             SubjectConsent.objects.get(subject_identifier=self.subject_identifier))
#         self.household_member = self.visit.household_member
#         self.appointments = self.visit.appointment.__class__.objects.filter(
#             subject_identifier=self.subject_identifier)
#         self.request = RequestFactory().get('/')
#         self.request.user = 'erik'
#
#     def test_survey(self):
#
#         class Dummy(BcppDashboardExtraFieldMixin, TemplateView):
#             template_name = 'bcpp_subject/dashboard.html'
#             consent_model = SubjectConsent
#
#         survey_object = self.subject_consent.survey_object
#         kwargs = {
#             'subject_identifier': self.subject_identifier,
#             'survey': survey_object.field_value}
#         response = Dummy.as_view()(self.request, **kwargs)
#         self.assertEqual(
#             response.context_data.get('survey'), survey_object)
#
#     def test_household_member(self):
#
#         class Dummy(BcppDashboardExtraFieldMixin, TemplateView):
#             template_name = 'bcpp_subject/dashboard.html'
#             consent_model = SubjectConsent
#
#         survey_object = self.subject_consent.survey_object
#         kwargs = {
#             'subject_identifier': self.subject_identifier,
#             'survey': survey_object.field_value,
#             'household_member': self.household_member.id}
#         response = Dummy.as_view()(self.request, **kwargs)
#         self.assertEqual(
#             response.context_data.get('household_member'), self.household_member)
#
#     def test_appointments(self):
#
#         class Dummy(BcppDashboardExtraFieldMixin, TemplateView):
#             template_name = 'bcpp_subject/dashboard.html'
#             consent_model = SubjectConsent
#
#         survey_object = self.subject_consent.survey_object
#         kwargs = {
#             'subject_identifier': self.subject_identifier,
#             'survey': survey_object.field_value,
#             'household_member': self.household_member.id,
#             'appointment': self.appointment.id}
#         response = Dummy.as_view()(self.request, **kwargs)
#         self.assertEqual(
#             len(response.context_data.get('apppointments')),
#             self.apppointments.count())
#         self.assertEqual(
#             response.context_data.get('apppointment'),
#             self.apppointments)
#
#     def test_survey2(self):
#         class Dummy(DashboardView, TemplateView):
#             template_name = 'bcpp_subject/dashboard.html'
#             consent_model = SubjectConsent
#
#         survey_object = self.subject_consent.survey_object
#         kwargs = {
#             'subject_identifier': self.subject_identifier,
#             'survey_name': survey_object.field_value}
#         response = Dummy.as_view()(self.request, **kwargs)
#         self.assertEqual(
#             response.context_data.get('survey_name'), survey_object.field_value)
#         self.assertEqual(
#             response.context_data.get('survey'), survey_object)
