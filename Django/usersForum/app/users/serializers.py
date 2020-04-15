from django.conf.urls import url, include
from django.contrib.auth import authenticate
from .models import User_model
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_model
        fields = (
            'id',
            'username',
            'image_url',
            'first_name',
            'last_name',
            'email',
            'facebook',
            'instagram',
            'twitter',
            'current_location',
            'is_active',
            'is_staff',
            'role',
            'is_verified',
            'created_at',
            'updated_at',
        )

class LoginSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    email = serializers.CharField(max_length=255)
    username = serializers.CharField(max_length=255, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    first_name = serializers.CharField(read_only=True)
    last_name = serializers.CharField(read_only=True)
    facebook = serializers.CharField(read_only=True)
    instagram = serializers.CharField(read_only=True)
    twitter = serializers.CharField(read_only=True)
    current_location = serializers.CharField(read_only=True)
    role = serializers.CharField(read_only=True)
    image_url = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):

        # The `validate` method is where we make sure that the current
        # instance of `LoginSerializer` has "valid".
        email = data.get('email', None)
        password = data.get('password', None)

        # Raise an exception if an email is not provided.
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )

        # Raise an exception if a password is not provided.
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )

        # The `authenticate` method is provided by Django and handles checking
        # for a user that matches this email/password combination.
        user = authenticate(email=email, password=password)
        # If no user was found matching this email/password combination then
        # `authenticate` will return `None`. Raise an exception in this case.
        if user is None:
            raise serializers.ValidationError(
                'Invalid email and/or password'
            )

        # Django provides a flag on our `User` model called `is_active`.
        if not user.is_active:
            raise serializers.ValidationError(
                'Invalid email and/or password'
            )

        # The `validate` method should return a dictionary of validated data.
        return {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'facebook': user.facebook,
            'instagram': user.instagram,
            'twitter': user.twitter,
            'current_location': user.current_location,
            'role': user.role,
            'is_verified': user.is_verified,
            'image_url': user.image_url,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
            'token': user.token
        }
