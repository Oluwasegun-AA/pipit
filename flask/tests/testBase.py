
# Method	Equivalent to
# .assertEqual(a, b)	a == b
# .assertTrue(x)	bool(x) is True
# .assertFalse(x)	bool(x) is False
# .assertIs(a, b)	a is b
# .assertIsNone(x)	x is None
# .assertIn(a, b)	a in b
# .assertIsInstance(a, b)	isinstance(a, b)

# test command
# python -m unittest test

# test suite auto discovery
# python -m unittest discover

# choosing a custom folder where the test cases are written
# python -m unittest discover -s tests -t src

# import subprocess
# subprocess.call(['','',''])
import unittest
import json
from app.server import createApp
from app.helpers.normalizeObj import normalize
# from app.database.dbSeed import InitDb

class TestBase(unittest.TestCase):

  def setUp(self):
    self.app = createApp()
    self.client = self.app.test_client()

  def post(self, route, jsonData={}, jwtToken = None):
    response = self.client.post(route,
      content_type="application/json",
      data=json.dumps(jsonData)
    )
    return json.loads(response.data)

  def get(self, route, jsonData={}, jwtToken = None):
    response = self.client.get(route,
      content_type="application/json",
      headers=dict(token = jwtToken),
      data=json.dumps(jsonData)
    )
    return json.loads(response.data)

  def put(self, route, jsonData, jwtToken = None):
    response = self.client.put(route,
      content_type="application/json",
      headers=dict(token=jwtToken),
      data=json.dumps(jsonData)
    )
    return json.loads(response.data)

  def patch(self, route, jsonData, jwtToken = None):
    response = self.client.patch(route,
      content_type="application/json",
      headers=dict(token=jwtToken),
      data=json.dumps(jsonData)
    )
    return json.loads(response.data)

  def delete(self, route, jsonData, jwtToken = None):
    response = self.client.delete(route,
      content_type="application/json",
      headers=dict(token=jwtToken),
      data=json.dumps(jsonData)
    )
    return json.loads(response.data)

  def getToken(self, username, password):
    res = self.post(
      '/api/v1/auth/login',
      {'username': username, 'password': password}
      )
    return res['token']
