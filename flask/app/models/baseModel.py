from app.database.dbSetup import SetupDb

class baseModel(object):
  def __init__(self):
    self.connection = SetupDb()
    self.cursor = self.connection.cursor()
