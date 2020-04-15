from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework import status, viewsets, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User_model
from .serializers import UserSerializer, LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from ..helpers.responseHandler import UserJSONRenderer
import json

def base(request):
  return JsonResponse({'status': 200, 'message':'Welcome to the Users forum'})

def pureDjangoGetUsers(request):
  users = User_model.objects.all()
  response = {"status": 200, "data": list(users.values("id","username","first_name","last_name","email","is_staff","is_verified","created_at","updated_at"))}
  return JsonResponse(response)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User_model.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

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
