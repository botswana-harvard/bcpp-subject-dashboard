from django.apps import AppConfig as DjangoApponfig


class AppConfig(DjangoApponfig):
    name = 'bcpp_subject_dashboard'

    listboard_template_name = 'bcpp_subject_dashboard/listboard.html'
    dashboard_template_name = 'bcpp_subject_dashboard/dashboard.html'

    listboard_url_name = 'bcpp_subject_dashboard:listboard_url'
    anonymous_listboard_url_name = 'bcpp_subject_dashboard:anonymous_listboard_url'
    dashboard_url_name = 'bcpp_subject_dashboard:dashboard_url'
    anonymous_dashboard_url_name = 'bcpp_subject_dashboard:anonymous_dashboard_url'
    admin_site_name = 'bcpp_subject_admin'
