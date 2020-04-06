# how to start sub app
# django-admin startapp app-name

from django.urls import path, include, re_path
from .views import baseError, routeError

urlpatterns = [
  path('', baseError),
  re_path(r'^.*/$', routeError)
]