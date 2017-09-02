from django.conf import settings

if settings.APP_NAME == 'bcpp_subject_dashboard':
    from .tests import models
