from django.urls import path

from . import views

app_name = 'equation'
urlpatterns = [
    path('', views.index, name='index'),
    ]