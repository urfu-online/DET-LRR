from django.contrib.admin.apps import AdminConfig


class LRRAdminConfig(AdminConfig):
    default_site = 'lrr.admin.LRRAdminSite'
