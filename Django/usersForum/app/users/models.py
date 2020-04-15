from  django.db import models
from uuid import uuid4
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from app.helpers.crypt import Password
import datetime
from ..helpers.tokenize import Tokenize

class UserManager(BaseUserManager):
  """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User` for free. 

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
  """

  def create_user(
        self, username,
        email,
        password=None,
        first_name='None', last_name='None',
        role ='U'
        ):
        """Create and return a `User` with an email, username and password."""

        if not (username and email and password):
            raise ValueError('Users must have an email, a username and a password.')
        
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            role=role,
            email=self.normalize_email(email)
        )
        user.set_password(password)

        user.save()

        return user

  def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser powers.

        Superuser powers means that this use is an admin that can do anything
        they want.
        """
        if password is None:
            raise ValueError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.first_name = 'Super'
        user.last_name = 'Admin'
        user.is_staff = True
        user.role = 'S'
        user.save()

        return user



class User_model(AbstractBaseUser, PermissionsMixin):
  id = models.UUIDField(
    primary_key=True,
    default=uuid4(),
    editable=False,
    unique=True
    )
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField(
    max_length=70,
    null=False,
    blank=False,
    unique=True
    )
  password = models.CharField(max_length=100)
  username = models.CharField(
    max_length=30,
    null=False,
    blank=False,
    unique=True
    )
  image_url = models.CharField(max_length=200, null=True)
  facebook = models.CharField(max_length=100, null=True)
  instagram = models.CharField(max_length=100, null=True)
  twitter = models.CharField(max_length=100, null=True)
  current_location = models.CharField(max_length=100, null=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  USERS = (
        ('Admin', 'Admin'),
        ('SuperAdmin', 'SuperAdmin'),
        ('User', 'User'),
    )
  role = models.CharField(max_length=10, choices=USERS, default='User')
  is_verified = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now_add=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['username']

  # Tells Django that the UserManager class defined above should manage
  # objects of this type.
  objects = UserManager()
  
  class Meta:
        db_table = 'Users'
  
  # returns a string/turple is none callable error in the django admin window when un-commented
  # @property
  # def __str__(self):
  #     return (self.first_name, self.last_name, f"({self.username})")
  
  @property
  def get_short_name(self):
      """
      This method is required by Django for things like handling emails.
      Typically, this would be the user's first name. Since we do not store
      the user's real name, we return their username instead.
      """
      return self.username
  @property
  def fullname(self):
      return f'{self.first_name} {self.last_name}'
  
  @property
  def token(self):
      """
      Generates the token and allows the token to be read via `user.token`
      : return string
      """
      return Tokenize.encrypt({"id": f'{self.pk}', "email": self.email})
