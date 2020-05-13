from rest_framework.test import APITestCase
from rest_framework.test import APIClient

class TestBase(APITestCase):
    def setUp(self):
      self.namespace = 'base'
      self.client = APIClient()
      self.noURI = ''
      self.invalidURI = 'invalid'

    def test_baseURL(self):
        noURIResponse = self.client.get(self.noURI)
        self.assertEqual(noURIResponse.status_code, 200)

    def test_error_route_on_baseURL(self):
        invalidURIResponse = self.client.get(self.invalidURI)
        self.assertEqual(invalidURIResponse.status_code, 404)