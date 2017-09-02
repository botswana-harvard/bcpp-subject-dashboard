from django.contrib.admin import AdminSite as DjangoAdminSite

from .models import SubjectConsent, SubjectLocator, Appointment
from .models import SubjectRequisition, SubjectVisit


class AdminSite(DjangoAdminSite):
    site_url = '/'


bcpp_subject_admin = AdminSite(name='bcpp_subject_admin')

bcpp_subject_admin.register(SubjectConsent)
bcpp_subject_admin.register(SubjectLocator)
bcpp_subject_admin.register(Appointment)
bcpp_subject_admin.register(SubjectVisit)
bcpp_subject_admin.register(SubjectRequisition)
