from app.models.baseModel import baseModel
from app.helpers.fetchData import fetch, fetchMany
from app.validations.checkUserExist import checkUserExist
# from app.validations.checkUserOwnsAccount import checkUserOwnsAccount

class UsersModel(baseModel):

  @checkUserExist
  def getUser(self, id):
    print('iiiii', id)
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    print('iiiii', data)
    return data

  def getAllUser(self):
    data = fetchMany(self.cursor, 'Users')
    return data
  
  @checkUserExist
  def updateUser(self, id, data):
    values = list(data.values())
    values.append(id)
    self.cursor.execute('''UPDATE "Users" SET username = (%s), email = (%s), "firstName" = (%s), "lastName" = (%s) WHERE id = (%s);''', values)
    self.connection.commit()
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    return data
  
  @checkUserExist
  def deleteUser(self, id):
    self.cursor.execute('''DELETE FROM "Users" WHERE id = (%s);''', [id])
    self.connection.commit()
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    return data
  
  @checkUserExist
  def makeAdmin(self, id, data):
    self.cursor.execute('''UPDATE "Users" SET "isAdmin" = (%s) WHERE id = (%s);''', [data['isAdmin'], id])
    self.connection.commit()
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    return data
  
  @checkUserExist
  def verifyUser(self, id):
    self.cursor.execute('''UPDATE "Users" SET verified = (%s) WHERE id = (%s);''', [True, id])
    self.connection.commit()
    data = fetch(self.cursor, 'Users', id, 'where id = (%s);')
    return data
