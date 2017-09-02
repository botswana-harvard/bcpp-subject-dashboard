from .model_wrapper_mixin import ModelWrapperMixin


class SubjectVisitModelWrapper(ModelWrapperMixin):

    model = 'bcpp_subject.subjectvisit'
    next_url_attrs = [
        'appointment', 'household_identifier', 'subject_identifier',
        'survey_schedule', 'survey']
    querystring_attrs = ['household_member']

    @property
    def household_member(self):
        return str(self.object.household_member.id)

    @property
    def appointment(self):
        return str(self.object.appointment.id)
