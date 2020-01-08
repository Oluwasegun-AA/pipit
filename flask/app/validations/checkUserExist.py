from app.helpers.fetchData import fetch
from app.database.dbSeed import SetupDb

connection = SetupDb()
cursor = connection.cursor()

def checkUserOwnsAccount(f):
    def check(*args, **kwargs):
      self, id = args
      if args[1]:
        data = fetch(cursor, 'Users', args[1], 'where id = (%s)')
        if 'error' in data.keys():
          return data
        elif data[id] is str(id) or data['isAdmin'] is True: 
          return f(*args, **kwargs)
        else:
          return {'status': 401, 'error': 'user not authorized'}
      else:
        return {'error': 'Bad request, invalid id'}
    return check