import json

from django.conf import settings
from django.core.management import BaseCommand

from mainapp.models import Lesson


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(
            settings.BASE_DIR / "mainapp/fixtures/003_lessons.json"
        ) as lessons_file:
            lessons_obj = json.load(lessons_file)
        lessons_list = []
        for lesson in lessons_obj:
            lessons_list.append(
                Lesson(
                    pk=lesson["pk"],
                    course=lesson["fields"]["course"],
                    num=lesson["fields"]["num"],
                    title=lesson["fields"]["title"],
                    description=lesson["fields"]["description"],
                    description_as_markdown=lesson["fields"][
                        "description_as_markdown"
                    ],
                    created_at=lesson["fields"]["created_at"],
                    updated_at=lesson["fields"]["updated_at"],
                )
            )
        Lesson.objects.bulk_create(lessons_list)
