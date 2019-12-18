import os

class Config(object):
  DEBUG= False
  TESTING= False
  DATABAE_URL= os.getenv('DATABAE_URL')

class Production():
  DEBUG= False
  TESTING= False
  DATABAE_URL= os.getenv('DATABAE_URL')

class Development():
  DEBUG= False
  TESTING= True
  DATABAE_URL= os.getenv('DATABAE_URL')

class Testing():
  DEBUG= True
  TESTING= True
  DATABAE_URL= os.getenv('DATABAE_URL')