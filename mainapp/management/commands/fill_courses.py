import json

from django.conf import settings
from django.core.management import BaseCommand

from mainapp.models import Course


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(
            settings.BASE_DIR / "mainapp/fixtures/002_courses.json"
        ) as courses_file:
            courses_obj = json.load(courses_file)
        courses_list = []
        for course in courses_obj:
            courses_list.append(
                Course(
                    pk=course["pk"],
                    name=course["fields"]["name"],
                    description=course["fields"]["description"],
                    description_as_markdown=course["fields"][
                        "description_as_markdown"
                    ],
                    cost=course["fields"]["cost"],
                    cover=course["fields"]["cover"],
                    created_at=course["fields"]["created_at"],
                    updated_at=course["fields"]["updated_at"],
                )
            )
        Course.objects.bulk_create(courses_list)
