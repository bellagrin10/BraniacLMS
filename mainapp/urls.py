from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('news/', views.NewsView.as_view(), name="news"),
    path('courses/', views.CoursesView.as_view(), name="courses"),
    path('contacts/', views.ContactsView.as_view(), name="contacts"),
    path('doc_site/', views.DocSiteView.as_view(), name="doc_site"),
    path('login/', views.LoginView.as_view(), name="login"),
]