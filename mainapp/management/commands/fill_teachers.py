import json

from django.conf import settings
from django.core.management import BaseCommand

from mainapp.models import CoursesTeacher


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(
            settings.BASE_DIR / "mainapp/fixtures/004_teachers.json"
        ) as teachers_file:
            teachers_obj = json.load(teachers_file)
        teachers_list = []
        for teacher in teachers_obj:
            teachers_list.append(
                CoursesTeacher(
                    pk=teacher["pk"],
                    name_first=teacher["fields"]["name_first"],
                    name_second=teacher["fields"]["name_second"],
                    day_birth=teacher["fields"]["day_birth"],
                    course=teacher["fields"]["course"],
                )
            )
        CoursesTeacher.objects.bulk_create(teachers_list)