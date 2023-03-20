from django.conf import settings
from django.contrib import admin


class LRRAdminSite(admin.AdminSite):
    label = 'LRRAdmin'
    site_header = 'Каталог ЦОТ (development)'
    if "det" in settings.INSTALLED_APPS:
        login_template = "det-admin/login.html"
        logout_template = "det-admin/logout.html"
        app_index_template = "det-admin/index.html"
        index_template = "det-admin/index.html"


if "adminactions" in settings.INSTALLED_APPS:
    from django.contrib.admin import site
    import adminactions.actions as actions

    actions.add_to_site(site)
