from django.conf.urls import url, include
from django.contrib.auth import authenticate
from .models import User_model
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_model
        fields = (
            'username',
            'image_url',
            'first_name',
            'last_name',
            'password',
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
            'token'
        )
        token = serializers.CharField(
        read_only=True
    )
        
    def validate(self, data):
      if not data:
        return serializers.ValidationError('Invalid data')

      email = data.get('email', None)
      username = data.get('username', None)
      password = data.get('password', None)

      if(self.context['method'] != 'update'):
        if (username or email or password) == None:
          raise serializers.ValidationError(
                'Email, username and password are required to signup.'
            )

        queryset = User_model.objects.filter(email=email)
      
        if queryset.exists():
          raise serializers.ValidationError('User already signed up')
      
      return data

    def create(self, validated_data):
      """
      Create a new instance of data
      """
      return User_model.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing data instance, given the validated data.
        """
        instance.username = validated_data.get('username', instance.username)
        instance.image_url = validated_data.get('image_url', instance.image_url)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.facebook = validated_data.get('facebook', instance.facebook)
        instance.instagram = validated_data.get('instagram', instance.instagram)
        instance.twitter = validated_data.get('twitter', instance.twitter)
        instance.current_location = validated_data.get('current_location', instance.current_location)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.role = validated_data.get('role', instance.role)
        instance.is_verified = validated_data.get('is_verified', instance.is_verified)
        instance.save()
        return instance
        

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
