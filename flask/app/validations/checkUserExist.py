from app.helpers.fetchData import fetch
from app.database.dbSeed import SetupDb
from flask import request
from app.helpers.tokenize import Tokenize

connection = SetupDb()
cursor = connection.cursor()

def checkUserExist(f):
    def check(*args, **kwargs):
      if args[1]:
        data = fetch(cursor, 'Users', str(args[1]), 'where id = (%s)')
        if 'error' in data.keys():
          return data
        else:
          return f(*args, **kwargs)
      else:
        return dict({'status': 400, 'error': 'Bad request, invalid user Id'}), 400
    return check