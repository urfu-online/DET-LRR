from django.http import HttpResponse
from django.views import View


class Favicon(View):
    def get(self, response):
        favicon_url = 'lrr/static/images/favicons/favicon.ico'
        with open(favicon_url, "rb") as f:
            return HttpResponse(f.read(), content_type="image/ico")
