from django.shortcuts import render
from django.http import HttpResponse
import json

def base(request):
  return HttpResponse(json.dumps({'status': 200, 'message':'Welcome to the Users forum'}))