import datetime
import os
from app.helpers.crypt import Password
from app.database.dbSetup import SetupDb

query = 'INSERT INTO "Users" (id,"firstName", "lastName", email, password, username, "isAdmin", verified, "createdAt", "updatedAt") VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'

users = [(
  '982a2372-f228-44c2-816a-3ef022e689fb',
  'Adepoju',
  'Oluwasegun',
  'oluwasegunadepoju@gmail.com',
  Password.encrypt('password'),
  'shegs',
  True,
  True,
  datetime.datetime.now(),
  datetime.datetime.now()
),
(
  'bbfa728f-f15b-4fc3-8a29-558236bb1008',
  'Njeri',
  'Ngigi',
  'njeri@gmail.com',
  Password.encrypt('password'),
  'shalon',
  False,
  False,
  datetime.datetime.now(),
  datetime.datetime.now()
),
(
  'd90f0e39-b5da-4377-8e33-b0f531414e6b',
  'Mirriam',
  'Maina',
  'mirriam@gmail.com',
  Password.encrypt('password'),
  'mirriam',
  False,
  False,
  datetime.datetime.now(),
  datetime.datetime.now()
),
(
  '1cf63969-6250-452e-9ae0-fa1dceca4ba5',
  'Theo',
  'Okafor',
  'theo@gmail.com',
  Password.encrypt('password'),
  'theo',
  False,
  False,
  datetime.datetime.now(),
  datetime.datetime.now()
),
(
  '6f13dcd6-49f0-4fba-a415-636b41c42888',
  'Eric',
  'Ebulu',
  'eric@gmail.com',
  Password.encrypt('password'),
  'eric',
  False,
  False,
  datetime.datetime.now(),
  datetime.datetime.now()
),
(
  '4cfd7015-7176-4e88-be1a-875f2e808646',
  'Kasule',
  'Joseph',
  'kasule@gmail.com',
  Password.encrypt('password'),
  'kasule',
  False,
  False,
  datetime.datetime.now(),
  datetime.datetime.now()
)]

class InitDb(object):

  def __init__(self):
    self.connection = SetupDb()
    self.cursor = self.connection.cursor()

  def dropTables(self):
     '''Drop all tables'''
     self.cursor.execute('''DROP TABLE IF EXISTS "Users";''')

  def createTables(self):
    if os.getenv('FLASK_ENV') == 'development':
      self.dropTables()

    '''method creating tables'''
    self.cursor.execute('''CREATE TABLE IF NOT EXISTS "Users"(
      id uuid PRIMARY KEY NOT NULL UNIQUE,
      username varchar(255) NOT NULL UNIQUE,
      "firstName" varchar(255) NOT NULL,
      "lastName" varchar(255) NOT NULL,
      email varchar(255) NOT NULL UNIQUE,
      password varchar(255) NOT NULL,
      "isAdmin" Boolean DEFAULT False,
      verified Boolean DEFAULT False,
      "createdAt" TIMESTAMP DEFAULT NOW(),
      "updatedAt" TIMESTAMP DEFAULT NULL
      );''')
      
    if os.getenv('FLASK_ENV') != 'development':
        self.closeConnection()

  def seedDb(self):
    if os.getenv('FLASK_ENV') == 'development':
      for user in users:
        self.cursor.execute(query, user)
      self.closeConnection()
  
  def closeConnection(self):
    self.connection.commit()
    self.cursor.close()
    self.connection.close()

