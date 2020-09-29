import json
# import the logging library
import logging
from urllib.request import urlopen

from django.core.management.base import BaseCommand, CommandError

from lrr.repository.models import DigitalResource

# Get an instance of a logger
logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'to import courses courses.openedu.urfu.ru via API [-p, --platform] - set PLATFORM URI [-u, --update] - ' \
           'set Flag -u if you want update(NOTE: Doesn"t work yet)'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--paltform', type=str)
        parser.add_argument('-u', '--update', type=str)

    def handle(self, *args, **kwargs):
        platform = kwargs['platform']
        update = kwargs['update']

        if platform == 'https://courses.openedu.urfu.ru/api/courses/v1/courses/?page_size=100':
            response = urlopen(platform)
            data = json.loads(response.read().decode("utf-8"))
            for course in data['results']:
                if update:
                    try:
                        digital_res = DigitalResource.objects.get(title=course['name'])
                        # TODO: which field to update?
                    except:
                        CommandError('DigitalResource does not exist')
                else:
                    if not DigitalResource.objects.filter(title=course['name']).exists():
                        digital_res = DigitalResource.objects.create(title=course['name'])
                        digital_res.save()
                        self.stdout.write(self.style.SUCCESS('Successfully DigitalResource created'))
        else:
            CommandError('Options does not exist')
