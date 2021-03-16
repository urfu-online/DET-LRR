from django.core.management.base import BaseCommand

from lrr.repository.models import DigitalResource, SubjectTag, Subject, \
    EduProgram, EduProgramTag


class Command(BaseCommand):
    help = "Write tags for recources."

    def handle(self, *args, **options):
        resources = DigitalResource.objects.all()
        subjects = Subject.objects.all()
        edu_programs = EduProgram.objects.filter(standard="ФГОС ВО")

        for subject in subjects:
            if not SubjectTag.objects.filter(tag=subject):
                SubjectTag.objects.create(tag=subject)

        for edu_program in edu_programs:
            if not EduProgramTag.objects.filter(tag=edu_program):
                EduProgramTag.objects.create(tag=edu_program)

        for resource in resources:
            for subject in subjects:
                if subject.title.lower() in resource.title.lower():
                    if not resource.subjects_tags.filter(tag__title=subject.title):
                        tag = SubjectTag.objects.get(tag=subject)
                        resource.subjects_tags.add(tag)
                        print(resource, tag)

            for edu_program in edu_programs:
                if edu_program.title.lower() in resource.title.lower():
                    if not resource.edu_programs_tags.filter(tag__title=edu_program.title):
                        tag = EduProgramTag.objects.get(tag=edu_program)
                        resource.edu_programs_tags.add(tag)
                        print(resource, tag)
