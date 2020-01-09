from app.helpers.fetchData import fetch
from app.database.dbSeed import SetupDb
from flask import request
from app.helpers.tokenize import Tokenize

connection = SetupDb()
cursor = connection.cursor()

def checkUserOwnsAccount(f):
    def check(*args, **kwargs):
      token = request.headers.get('token')
      dataInToken = Tokenize.decrypt(token)
      if args[1] and not 'error' in dataInToken:
        data = fetch(cursor, 'Users', str(args[1]), 'where id = (%s)')
        if 'error' in data.keys():
          return data
        elif (str(data['id']) == str(dataInToken['id'])) or dataInToken['isAdmin'] == 'True': 
          return f(*args, **kwargs)
        else:
          return dict({'status': 401, 'error': 'user not authorizedd'}), 401
      elif 'error' in dataInToken:
        return dict({'status': 401, 'error': 'User Unauthoorized'}), 401
      else:
        return dict({'status': 401, 'error': 'Bad request, invalid user Id'}), 401
    return check