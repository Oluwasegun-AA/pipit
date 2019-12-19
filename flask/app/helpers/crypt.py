import bcrypt

class Password:
  @staticmethod
  def encrypt(password):
    return bcrypt.hashpw(b'password', bcrypt.gensalt(10))

  @staticmethod
  def decrypt(password, hash):
    return bcrypt.checkpw(password, hash);
