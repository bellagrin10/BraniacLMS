import json

from django.conf import settings
from django.core.management import BaseCommand

from mainapp.models import News


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        with open(
            settings.BASE_DIR / "mainapp/fixtures/001_news.json"
        ) as news_file:
            news_obj = json.load(news_file)
        news_list = []
        for news in news_obj:
            news_list.append(
                News(
                    pk=news["pk"],
                    title=news["fields"]["title"],
                    preamble=news["fields"]["preamble"],
                    body=news["fields"]["body"],
                    body_as_markdown=news["fields"]["body_as_markdown"],
                    created_at=news["fields"]["created_at"],
                )
            )
        News.objects.bulk_create(news_list)
