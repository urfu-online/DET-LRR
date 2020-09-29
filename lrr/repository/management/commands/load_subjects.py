import os

from django.conf import settings
from django.core.management.base import BaseCommand

from lrr.repository.models import Subject


class Command(BaseCommand):
    help = "Load subjects to db."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        with open(os.path.join(settings.ROOT_DIR, 'scripts', "subjects"), "r") as f:
            for subject in f.readlines():
                existed_subjects = Subject.objects.filter(title=subject.strip())
                if not existed_subjects:
                    Subject.objects.create(title=subject.strip())
