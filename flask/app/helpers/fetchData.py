
from app.helpers.formatResponse import formatResponse

def fetch(cursor, table, value, query = 'where username = (%s);'):
   cursor.execute(f'''SELECT * FROM "{table}" {query}''', [value])
   result = cursor.fetchone()
   if result is None:
     return {'error': 'Data not found', 'status': 404}
   else:
     response = formatResponse.single(cursor.description, result)
     return response

def fetchMany(cursor, table, query = ''):
   cursor.execute(f'''SELECT * FROM "{table}" {query}''')
   result = cursor.fetchall()
   if result is None:
     return {'error': 'Data not found', 'status': 404}
   else:
     response = formatResponse.multiple(cursor.description, result)
     return response
