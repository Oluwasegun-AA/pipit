import psycopg2
import os
from ..helpers.env import getEnvironmentConfig

def SetupDb():
  return psycopg2.connect(os.getenv('DATABASE_URL'))
