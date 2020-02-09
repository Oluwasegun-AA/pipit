from  django.db import models
from uuid import uuid4

class User_model(models.Model):
  id = models.UUIDField(primary_key=True, default=uuid4(), editable=False)
  firstName = models.CharField(max_length=30)
  lastName = models.CharField(max_length=30)
  email = models.EmailField(max_length=70, null=False, blank=False, unique=True)
  password = models.CharField(max_length=30)
  username = models.CharField(max_length=30)
  isAdmin = models.BooleanField(default=False)
  verified = models.BooleanField(default=False)
  createdAt = models.DateTimeField(auto_now_add=True)
  updatedAt = models.DateTimeField(auto_now_add=True)

  class Meta:
        db_table = 'Users'