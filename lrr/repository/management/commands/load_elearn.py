import json
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from lrr.repository.models import DigitalResource, Platform, Organization, Language, Source


class Command(BaseCommand):
    help = "Load elearn recources to db."

    #  DigitalResource.objects.filter(platform=Platform.objects.get(title="Портал электронного обучения")).delete()
    # DigitalResource.get_resources_by_subject(s[0])
    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        with open(os.path.join(settings.ROOT_DIR, 'scripts', 'elearn', "elearn_mdl_course.json"), 'r') as f:
            elearn_courses = json.load(f)

            elearn_platform = Platform.objects.filter(title="Портал электронного обучения")[0]
            elearn_org = Organization.objects.filter(title="УрФУ")[0]
            if not elearn_platform:
                raise Exception("Платформа не найдена")
            if not elearn_org:
                raise Exception("Образовательная организация не найдена")

            for course in elearn_courses:
                digital_resource = DigitalResource.objects.filter(platform=elearn_platform,
                                                                  title=course["fullname"].strip())
                if course["lang"] != '':
                    language = Language.objects.get(code=course["lang"])
                else:
                    language = Language.objects.get(code='ru')

                if not digital_resource and course["visible"] == 1:
                    digital_resource = DigitalResource.objects.create(
                        title=course["fullname"].strip(),
                        platform=elearn_platform,
                        copyright_holder=elearn_org,
                        language=language,
                        description=course["summary"],

                        type=DigitalResource.EUK,
                        source_data=DigitalResource.IMPORT
                    )
                    Source.objects.create(
                        URL=f"https://elearn.urfu.ru/course/view.php?id={course['id']}",
                        digital_resource=digital_resource
                    )

                    print(course["fullname"].strip())
