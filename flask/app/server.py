import os
from flask import Flask, Blueprint
from .helpers.env import getEnvironmentConfig
from .database.dbSetup import SetupDb
from app.database.dbSeed import InitDb
from app.helpers.catchRouteErrors import catchRouteErrors
from app.views import addResources

def createApp():
  APP = Flask(__name__)
  APP.config.from_object(getEnvironmentConfig())
  APP.url_map.strict_slashes = False
  addResources(APP)
  catchRouteErrors(APP)
  database = SetupDb()

  if os.getenv('FLASK_ENV') == 'development':
    database = InitDb()
    database.createTables()
    database.seedDb()
  else: 
    database = InitDb().createTables()

  return APP
