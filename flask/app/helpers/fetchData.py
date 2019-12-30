
from app.helpers.formatResponse import formatResponse

def fetch(cursor, table, value):
   cursor.execute(f'''SELECT * FROM "{table}" where username = (%s);''', [value])
   result = cursor.fetchone()
   if result is None:
     return {'error': 'Data not found', 'status': 404}
   else:
     response = formatResponse.single(cursor.description, result)
     return response
     