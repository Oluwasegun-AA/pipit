def checkUserExist(f):
    def check(*args, **kwargs):
      self, id = args
      if args[1]:
        data = fetch(cursor, 'Users', args[1], 'where id = (%s)')
        if 'error' in data.keys():
          return {'lll':data}
        else: return f(*args, **kwargs)
      else:
        return {'error': 'Bad request, invalid id'}
    return check