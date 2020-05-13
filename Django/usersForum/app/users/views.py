from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import status, viewsets, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User_model
from .serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..helpers.responseHandler import UserJSONRenderer
from .permissions import IsAdminReadAndWriteOnly, IsAdminOrOwnsAccount
from ..helpers.customObj import omit
import json

def base(request):
  return JsonResponse({'status': 200, 'message':'Welcome to the Users forum'})

def pureDjangoGetUsers(request):
  users = User_model.objects.all()
  response = {"status": 200, "data": list(users.values("id","username","first_name","last_name","email","is_staff","is_verified","created_at","updated_at"))}
  return JsonResponse(response)

def setPermissions(self):
  if self.action == 'create':
    return [AllowAny()]            
  elif self.action == 'list':
    return [IsAuthenticated(), IsAdminReadAndWriteOnly()]
  return [IsAuthenticated(), IsAdminOrOwnsAccount()]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User_model.objects.none()
    serializer = UserSerializer

    def get_permissions(self):
       return setPermissions(self)

    def create(self, request):
      user = request.data.get('user', None)
      serializer = self.serializer(data=user, context={'method': 'create'})
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({'message': 'User created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    
    def list(self, request):
      # get all users
      self.check_object_permissions(request, obj={})
      users = User_model.objects.all().order_by('username')
      data = self.serializer(users, many=True, context={'method': 'list'}).data
      return Response({'message': 'Data retrieved successfully', 'data':omit(data, ['password', 'token'])}, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
      # get one user
      self.check_object_permissions(request, {"id":pk})
      queryset = User_model.objects.get(pk=pk)
      data = self.serializer(queryset, context={'method': 'retrieve'}).data
      return Response({'message': 'Data retrieved successfully', 'data':omit(data, ['token', 'password'])}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
      # update a user (put)
      self.check_object_permissions(request, {"id":pk})
      data = request.data

      try:
        instance = User_model.objects.get(pk=pk)
      except User_model.DoesNotExist:
        return Response({'message': 'user not found'},
                            status=status.HTTP_404_NOT_FOUND)

      serializer = self.serializer(instance, data=data, partial=True, context={'method': 'update'})
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({'message':'User updated successfully', 'data': omit(serializer.data, ['token', 'password'])}, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
      # update a user (patch)
      self.check_object_permissions(request, {"id":pk})
      data = request.data

      try:
        instance = User_model.objects.get(pk=pk)
      except User_model.DoesNotExist:
        return Response({'message': 'user not found'},
                            status=status.HTTP_404_NOT_FOUND)

      serializer = self.serializer(instance, data=data, partial=True, context={'method': 'update'})
      serializer.is_valid(raise_exception=True)
      serializer.save()
      return Response({'message':'user updated successfully', 'data': omit(serializer.data, ['token', 'password'])}, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None):
      # delete a user
      self.check_object_permissions(request, {"id":pk})

      try:
        instance = User_model.objects.get(pk=pk)
      except User_model.DoesNotExist:
        return Response({'message': 'User not found'},
                            status=status.HTTP_404_NOT_FOUND)
      
      try:
        instance.delete()
      except User_model.DoesNotExist:
        return Response({'message': 'Error deleting User'},
                            status=status.is_server_error)
      return Response({'message':'User deleted successfully'}, status=status.HTTP_200_OK)

class LoginAPIView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def post(self, request):
        user = request.data.get('user', {})

        # Notice here that we do not call `serializer.save()` like we did for
        # the registration endpoint. This is because we don't actually have
        # anything to save. Instead, the `validate` method on our serializer
        # handles everything we need.
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
