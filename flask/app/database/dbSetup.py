import psycopg2
import os
from app.helpers.env import getEnvironmentConfig

def SetupDb():
  return psycopg2.connect(dbname='flask', user='postgres', host='localhost')
