# {cfg.proj_name}/core/urls.py

from django.urls import path

from . import views


urlpatterns = [

    path('', views.home, name='home'),

]
