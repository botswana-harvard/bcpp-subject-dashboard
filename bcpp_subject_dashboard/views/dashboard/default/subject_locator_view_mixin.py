from django.apps import apps as django_apps

from ...wrappers import SubjectLocatorModelWrapper


class SubjectLocatorViewMixin:

    subject_locator_model_wrapper_class = SubjectLocatorModelWrapper
    subject_locator_model = 'bcpp_subject.subjectlocator'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subject_locator = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.subject_locator = self.subject_locator_model_wrapper
        context.update(subject_locator=self.subject_locator)
        return context

    def get_subject_locator(self):
        """Returns a model instance either saved or unsaved.

        If a save instance does not exits, returns a new unsaved instance.
        """
        SubjectLocator = django_apps.get_model(self.subject_locator_model)
        try:
            subject_locator = SubjectLocator.objects.get(
                subject_identifier=self.subject_identifier)
        except SubjectLocator.DoesNotExist:
            subject_locator = SubjectLocator(
                subject_identifier=self.subject_identifier)
        return subject_locator

    @property
    def subject_locator_model_wrapper(self):
        """Returns a model wrapper instance of the subject locator.
        """
        return self.subject_locator_model_wrapper_class(
            self.get_subject_locator(),
            household_identifier=self.household_identifier,
            survey_schedule=self.survey_schedule_object.field_value)
