from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from .views import base, pureDjangoGetUsers, UserViewSet, LoginAPIView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
  path('', include(router.urls)),
  path('', base),
  path('djangoGet', pureDjangoGetUsers),
  path('login', LoginAPIView.as_view(), name='login'),
]