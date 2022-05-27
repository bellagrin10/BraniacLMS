from django.shortcuts import render

import requests
from black import Any, Dict

from django.views.generic import TemplateView
from datetime import datetime

import os
from dotenv import load_dotenv

load_dotenv()

class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        
        # 3. На странице новостей организуйте цикл, где выводятся карточки новостей (5 одинаковых карточек).

        context = super().get_context_data(**kwargs)
        context['range'] = range(1, 6)
        context['new'] = {
            'title': 'Новостной заголовок',
            'preview': ['Предварительное описание', '-й новости'],
            'date': datetime.now()
        }

        # 6. (*) Сформируйте JSON-файл и разместите в нём несколько сгенерированных новостей с заголовками, 
        # Затем выведите их в цикле на странице новостей. 

        API_KEY = str(os.getenv('API_KEY'))
          
        url=f'https://newsapi.org/v2/top-headlines?country=ru&category=technology&apiKey={API_KEY}'
        news = requests.get(url).json()
        
        new_title = []
        description = []
        img = []
        publishedAt = []
        
        for new in news['articles']:
            new_title.append(new['title'])
            description.append(new['description'])
            img.append(new['urlToImage'])
            publishedAt.append(new['publishedAt'])

        context['myNewscast'] = zip(new_title, description, img, publishedAt)

        return context


class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:

        context = super().get_context_data(**kwargs)

        map = [
            'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA', 
            'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB', 
            'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD', 
        ]
        city = ['Санкт‑Петербург', 'Казань', 'Москва', ]
        phone = ['+7-999-11-11111', '+7-999-22-22222', '+7-999-33-33333', ]
        email = ['geeklab@spb.ru', 'geeklab@kz.ru', 'geeklab@msk.ru', ]
        address = [
            'территория Петропавловская крепость, 3Ж', 
            'территория Кремль, 11, Казань, Республика Татарстан, Россия', 
            'Красная площадь, 7, Москва, Россия', 
        ]
        context['contacts'] = zip(map, city, phone, email, address)
        
        return context


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'


