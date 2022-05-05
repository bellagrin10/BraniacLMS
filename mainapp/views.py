#from django.shortcuts import render

from black import Any, Dict
from django.views.generic import TemplateView
from datetime import datetime

class MainPageView(TemplateView):
    template_name = 'mainapp/index.html'


class NewsPageView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['range'] = range(1, 6)
        context['new'] = {
            'title': 'Новостной заголовок',
            'preview': ['Предварительное описание', '-й новости'],
            'date': datetime.now()
        }
        return context

class CoursesPageView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class ContactsPageView(TemplateView):
    template_name = 'mainapp/contacts.html'


class DocSitePageView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class LoginPageView(TemplateView):
    template_name = 'mainapp/login.html'


