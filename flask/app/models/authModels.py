from flask import jsonify
from app.models.baseModel import baseModel
from app.helpers.formatResponse import formatResponse
from app.helpers.fetchData import fetch
from uuid import uuid4
from app.helpers.crypt import Password
from app.helpers.pick import pick

class authModel(baseModel):

  def login(self, data):
    self.cursor.execute('SELECT * FROM "Users" where username = (%s);', [data['username']])
    result = self.cursor.fetchone()
    if result is None:
      return {'message': 'Bad request, user not found', 'status': 404}
    else:
      response = formatResponse.single(self.cursor.description, result)
      if Password.decrypt(data['password'], response['password']):
        return {'status': 200, 'message': 'login successful', 'token': pick(response, ['id', 'username', 'email'])}
      else: return {'status': 400, 'error': 'invalid username or password'}
  
  def signup(self, data):
    self.cursor.execute('INSERT INTO "Users" (id,"firstName", "lastName", email, password, username, "isAdmin", verified) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)', [str(uuid4()), *list(data.values())])
    self.connection.commit()
    data = fetch(self.cursor, 'Users', data['username'])
    if 'error' in data.keys():
      return {'status': 500, 'error': 'Internal server error, user not created'}
    else:
      return {'status': 200, 'data': data}
