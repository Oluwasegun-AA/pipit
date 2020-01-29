from app.models.baseModel import baseModel
from app.helpers.fetchData import fetch, fetchMany
from app.validations.checkUserExist import checkUserExist
from app.validations.checkUserOwnsAccount import checkUserOwnsAccount
from app.validations.checkAdminInToken import checkAdminInToken
from app.validations.checkTokenIsValid import checkTokenIsValid
from app.helpers.normalizeObj import normalize

class UsersModel(baseModel):

  @checkTokenIsValid
  # @checkUserExist
  # @checkAdminInToken
  def getUser(self, id):
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    return dict({'status': 200, 'message':'data retrieved successfully', 'data': normalize(data)}), 200

  @checkAdminInToken
  def getAllUser(self):
    data = fetchMany(self.cursor, 'Users')
    return normalize(data), 200
  
  @checkTokenIsValid
  @checkUserExist
  @checkUserOwnsAccount
  def updateUser(self, id, data):
    values = list(data.values())
    values.append(id)
    self.cursor.execute('''UPDATE "Users" SET username = (%s), email = (%s), "firstName" = (%s), "lastName" = (%s) WHERE id = (%s);''', values)
    self.connection.commit()
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    return normalize(data)
  
  @checkTokenIsValid
  @checkUserExist
  @checkUserOwnsAccount
  def deleteUser(self, id):
    self.cursor.execute('''DELETE FROM "Users" WHERE id = (%s);''', [id])
    self.connection.commit()
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    return data
  
  @checkTokenIsValid
  @checkUserExist
  @checkAdminInToken
  def makeAdmin(self, id, data):
    self.cursor.execute('''UPDATE "Users" SET "isAdmin" = (%s) WHERE id = (%s);''', [data['isAdmin'], id])
    self.connection.commit()
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    return data
  
  @checkTokenIsValid
  @checkUserExist
  @checkAdminInToken
  def verifyUser(self, id):
    self.cursor.execute('''UPDATE "Users" SET verified = (%s) WHERE id = (%s);''', [True, id])
    self.connection.commit()
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    return data
