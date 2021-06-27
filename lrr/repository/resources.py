from import_export import resources
from lrr.repository.models import DigitalResource


class DigitalResourceResource(resources.ModelResource):
    class Meta:
        model = DigitalResource
        fields = "__all__"
