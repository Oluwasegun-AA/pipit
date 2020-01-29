'''app/views/__init__.py'''
from app.views.authViews import auth, signup
from app.views.usersViews import (User, GetAllUser, VerifyUser, makeAdmin)
from flask_restful import Api
import os

def addResources(app):
  BASE = os.getenv('BASE_URL')
  api = Api(app, prefix='/api/v1', catch_all_404s=True)
  api.add_resource(auth, '/auth/login')
  api.add_resource(signup, '/auth/signup')
  api.add_resource(User, '/user', '/user/<id>/')
  api.add_resource(GetAllUser, '/users')
  api.add_resource(VerifyUser, '/user/verify/<id>')
  api.add_resource(makeAdmin, '/user/authorize/<id>')
