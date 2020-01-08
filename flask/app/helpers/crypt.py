import bcrypt

class Password:
  @staticmethod
  def encrypt(password):
    hash = bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())
    return hash.decode('utf-8')

  @staticmethod
  def decrypt(password, hash):
    return bcrypt.checkpw(bytes(password, 'utf-8'), bytes(hash, 'utf-8'))
