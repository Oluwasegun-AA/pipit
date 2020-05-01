'''app/views/__init__.py'''
from app.views.authViews import auth, signup
from flask_restful import Api
import os

def addResources(app):
  BASE = os.getenv('BASEURL')
  api = Api(app, catch_all_404s=True)
  api.add_resource(auth, BASE+'/login')
  api.add_resource(signup, BASE+'/signup')