from app.helpers.fetchData import fetch
from app.database.dbSeed import SetupDb
from flask import request
from app.helpers.tokenize import Tokenize

connection = SetupDb()
cursor = connection.cursor()

def checkAdminInToken(f):
  def check(*args, **kwargs):
    token = request.headers.get('token')
    dataInToken = Tokenize.decrypt(token)
    if 'isAdmin' in dataInToken:
      if dataInToken['isAdmin'] == 'False':
        return {'error': 401, 'error': 'User Unauthorized'}
      else:
        return f(*args, **kwargs)
    else:
      return {'error': 401, 'error': 'User Unauthorized'}
    
  return check