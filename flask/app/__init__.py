'''app/__init__.py'''

import os
from flask import Flask
from .helpers.env import getEnvironmentConfig
from .database.dbSetup import SetupDb
from app.database.dbSeed import InitDb

def createApp():
  APP = Flask(__name__)
  APP.config.from_object(getEnvironmentConfig())
  APP.url_map.strict_slashes = False
  database = SetupDb()

  if os.getenv('FLASK_ENV') == 'development':
    database = InitDb()
    database.createTables()
    database.seedDb()
  else: 
    database = InitDb().createTables()

  return APP

