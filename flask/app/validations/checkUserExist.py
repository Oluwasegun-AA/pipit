from app.helpers.fetchData import fetch
from app.database.dbSeed import SetupDb
from flask import request
from app.helpers.tokenize import Tokenize

connection = SetupDb()
cursor = connection.cursor()

def checkUserExist(f):
    def check(*args, **kwargs):
      token = request.headers.get('token')
      dataInToken = Tokenize.decrypt(token)
      if args[1]:
        data = fetch(cursor, 'Users', str(args[1]), 'where id = (%s)')
        if 'error' in data.keys():
          return data
        elif (str(data['id']) == str(dataInToken['id'])) or dataInToken['isAdmin'] == True: 
          return f(*args, **kwargs)
        else:
          return {'status': 401, 'error': 'user not authorized'}
      else:
        return {'error': 'Bad request, invalid id'}
    return check