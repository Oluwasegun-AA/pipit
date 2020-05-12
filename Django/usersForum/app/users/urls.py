from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter
from rest_framework import routers
from django.urls import path
from .views import base, pureDjangoGetUsers, UserViewSet, LoginAPIView

class OptionalSlashRouter(SimpleRouter):
  
    def __init__(self):
        self.trailing_slash = '/?'
        super(SimpleRouter, self).__init__()
        
router = OptionalSlashRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
  # path('users', CreateUserAPIView.as_view(), name='register'),
  path('', include(router.urls)),
  path('', base),
  path('djangoGet', pureDjangoGetUsers),
  path('login', LoginAPIView.as_view(), name='login'),
]
