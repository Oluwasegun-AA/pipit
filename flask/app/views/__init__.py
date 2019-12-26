'''app/views/__init__.py'''
from app.views.authViews import auth, signup
from flask_restful import Api

def addResources(app):
   api = Api(app, catch_all_404s=True)
   api.add_resource(auth, '/login')
   api.add_resource(signup, '/signup')