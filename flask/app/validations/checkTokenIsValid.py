from app.helpers.fetchData import fetch
from app.database.dbSeed import SetupDb
from flask import request
from app.helpers.tokenize import Tokenize

connection = SetupDb()
cursor = connection.cursor()

def checkTokenIsValid(f):
    def check(*args, **kwargs):
      token = request.headers.get('token')
      dataInToken = Tokenize.decrypt(token)
      if 'error' in dataInToken:
        return dict({'error': 401, 'error': 'User Unauthorized'}), 401
      else:
        return f(*args, **kwargs)
    return check