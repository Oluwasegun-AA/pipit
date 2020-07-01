'''app/views/__init__.py'''
from app.views.authViews import auth, signup
from app.views.usersViews import (User, GetAllUser, VerifyUser, makeAdmin)
from flask_restful import Api
import os

def addResources(app):
  BASE = os.getenv('BASE_URL')
  api = Api(app, catch_all_404s=True)
  api.add_resource(auth, BASE+'/login')
  api.add_resource(signup, BASE+'/signup')

  api.add_resource(User, BASE+'/user', BASE+'/user/<id>/')
  api.add_resource(GetAllUser, BASE+'/users')
  api.add_resource(VerifyUser, BASE+'/user/verify/<id>')
  api.add_resource(makeAdmin, BASE+'/user/authorize/<id>')
