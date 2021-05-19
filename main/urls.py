from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main, name='main'),
    path('cabinet', views.cabinet, name='cabinet'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]
