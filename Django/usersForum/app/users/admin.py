from django.contrib import admin
from django.contrib.auth import get_user_model

user = get_user_model()
admin.site.register(user)
# Register your models here.
