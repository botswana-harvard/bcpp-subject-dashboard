from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'bcpp_subject_dashboard'

    base_template_name = 'edc_base/base.html'

    dashboard_template_name = 'bcpp_subject_dashboard/dashboard.html'
    listboard_template_name = 'bcpp_subject_dashboard/listboard.html'

    admin_site_name = 'bcpp_subject_admin'
    anonymous_dashboard_url_name = 'bcpp_subject_dashboard:anonymous_dashboard_url'
    anonymous_listboard_url_name = 'bcpp_subject_dashboard:anonymous_listboard_url'
    dashboard_url_name = 'bcpp_subject_dashboard:dashboard_url'
    listboard_url_name = 'bcpp_subject_dashboard:listboard_url'
