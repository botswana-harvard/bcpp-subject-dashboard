from django.db import models
from edc_base.model_mixins import BaseUuidModel
from survey.model_mixins import SurveyModelMixin, SurveyScheduleModelMixin
from edc_constants.constants import MALE


class Plot(BaseUuidModel):

    plot_identifier = models.CharField(max_length=25)


class Household(BaseUuidModel):

    household_identifier = models.CharField(max_length=25)

    plot = models.ForeignKey(
        Plot, on_delete=models.PROTECT)


class HouseholdStructure(SurveyScheduleModelMixin, BaseUuidModel):

    household = models.ForeignKey(
        Household, on_delete=models.PROTECT)


class HouseholdMember(SurveyScheduleModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    first_name = models.CharField(max_length=25, default='NOAM')

    age_in_years = models.IntegerField(default=25)

    gender = models.CharField(max_length=25, default=MALE)

    household_structure = models.ForeignKey(
        HouseholdStructure, on_delete=models.PROTECT)


class Appointment(SurveyModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    household_member = models.ForeignKey(
        HouseholdMember, on_delete=models.PROTECT)


class SubjectVisit(SurveyModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    appointment = models.OneToOneField(Appointment)

    household_member = models.ForeignKey(
        HouseholdMember, on_delete=models.PROTECT)


class SubjectRequisition(SurveyModelMixin, BaseUuidModel):

    subject_visit = models.ForeignKey(SubjectVisit)

    panel_name = models.CharField(max_length=25)


class SubjectConsent(SurveyModelMixin, BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)

    gender = models.CharField(max_length=25, default='M')

    initials = models.CharField(max_length=25, default='XX')

    first_name = models.CharField(max_length=25, default='NOAM')

    household_member = models.ForeignKey(
        HouseholdMember, on_delete=models.PROTECT)


class SubjectLocator(BaseUuidModel):

    subject_identifier = models.CharField(max_length=25)
