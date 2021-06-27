import csv

from django.core.management.base import BaseCommand

from lrr.repository.models import EduProgram, Direction


class Command(BaseCommand):
    help = "Load programs form programs.csv file."

    def handle(self, *args, **options):
        with open("lrr/data/programs.csv") as f:
            reader = csv.DictReader(f, delimiter=";")
            for row in reader:
                direction = Direction.by_code(
                    row.get("Код направления").replace("\'", ""))  # TODO: make remove quotes util
                admission_years = row.get("Годы приёма").split(", ")
                cipher = row.get("Шифр ОП")[-5:]
                eduprogram = EduProgram(
                    title=row.get("Название ОП"),
                    standard=row.get("Стандарт"),
                    edu_level=row.get("Уровень подготовки"),
                    _cipher=cipher,

                    approve_year=row.get("Год утв. ОП"),
                    head=row.get("Руководитель ОП"),
                    site_admin=row.get("Администратор сайта ОП"),

                    direction=direction
                )
                if admission_years != [""]:
                    eduprogram.admission_years = admission_years
                eduprogram.save()
                print(eduprogram)
