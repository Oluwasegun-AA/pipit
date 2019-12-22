import os

class Config(object):
  DEBUG= False
  TESTING= False

class Production(object):
  DEBUG= False
  TESTING= False

class Development(object):
  DEBUG= False
  TESTING= True

class Testing(object):
  DEBUG= True
  TESTING= True