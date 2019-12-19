import os
from instance.config import (Development, Testing, Production)

def getEnvironmentConfig():
  if os.getenv('FLASK_ENV') == 'development':
    return Development
  elif os.getenv('FLASK_ENV') == 'production':
    return Production
  else: return Testing