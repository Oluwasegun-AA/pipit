from django.shortcuts import render
from django.http import JsonResponse

def baseError(request):
  return JsonResponse({
    'status': 200,
    'message': 'Welcome to the Users forum, please consume the API via api/v1'
    })
    
def routeError(request):
  return JsonResponse({
    'status': 400,
    'message': f'invalid route "{request.path}", please checkout the API documentation via "api/vi/docs"'
    })