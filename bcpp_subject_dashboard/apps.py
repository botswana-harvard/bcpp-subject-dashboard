from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'bcpp_subject_dashboard'
    listboard_template_name = 'bcpp_subject_dashboard/listboard.html'
    listboard_url_name = 'bcpp_subject_dashboard:listboard_url'
    base_template_name = 'edc_base/base.html'
    url_namespace = 'bcpp_subject_dashboard'
    anonymous_listboard_url_name = 'bcpp_subject_dashboard:anonymous_listboard_url'
