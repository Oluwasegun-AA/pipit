from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from decouple import config

class TestUsers(APITestCase):
    fixtures = ['users.json']

    def setUp(self):
      self.namespace = 'users'
      self.client = APIClient()
      self.loginURI = '/api/v1/login'
      self.postUserURI = '/api/v1/users'
      self.djangoGetAllURI = '/api/v1/djangoGet'
      self.listUserURI = '/api/v1/users/d90f0e39-b5da-4377-8e33-b0f531414e6b' #kasule
      self.listAllUserURI = '/api/v1/users'
      self.updateUserURI = '/api/v1/users/6f13dcd6-49f0-4fba-a415-636b41c42888' #eric
      self.partialUpdateUserURI = '/api/v1/users/6f13dcd6-49f0-4fba-a415-636b41c42888' #eric
      self.deleteUserURI = '/api/v1/users/4cfd7015-7176-4e88-be1a-875f2e808646' #mirriam

      self.adminLoginData = {
            'user': {
                'email': 'shegsteham@gmail.com',
                'password': 'shegsteham',
            }
        }

      self.userLoginData = {
            'user': {
                'email': 'mirriam@gmail.com',
                'password': 'shegsteham',
            }
        }

      self.validPostUserdata = {
          'user': {
              'username': 'testUsername',
              'first_name': 'testFirstName',
              'last_name': 'testLastName',
              'email': 'testEmail@gmail.com',
              'password': 'test',
              'role': 'SuperAdmin',
              'created_at': '2020-04-06T04:46:36.797000+01:00',
              'updated_at': '2020-04-06T04:46:36.797000+01:00'
          }
      }

      self.invalidPostUserdata = {
          'user': {
              'first_name': 'testFirstName',
              'last_name': 'testLastName',
              'email': 'testEmail@gmail.com',
              'password': 'test',
              'role': 'SuperAdmin',
              'created_at': '2020-04-06T04:46:36.797000+01:00',
              'updated_at': '2020-04-06T04:46:36.797000+01:00'
          }
      }

      self.validUserUpdateData = {
              'username': 'testUsername',
              'first_name': 'testFirstName',
              'last_name': 'testLastName',
              'email': 'testEmail@gmail.com',
              'password': 'test',
              'role': 'SuperAdmin',
              'created_at': '2020-04-06T04:46:36.797000+01:00',
              'updated_at': '2020-04-06T04:46:36.797000+01:00'
          }

      self.adminData = self.client.post(self.loginURI, self.adminLoginData, format='json')
      self.userData = self.client.post(self.loginURI, self.userLoginData, format='json')
    

    def test_login(self):
      self.assertEqual(self.adminData.status_code, 200)
      self.assertEqual(self.adminData.data['id'], '56a55cf7-696c-4709-8607-e4935a37b8c1')
      self.assertEqual(self.adminData.data['role'], 'SuperAdmin')
      self.assertEqual(self.adminData.data['username'], 'shegsteham')
      self.assertEqual(self.userData.status_code, 200)
      self.assertEqual(self.userData.data['id'], 'd90f0e39-b5da-4377-8e33-b0f531414e6b')
      self.assertEqual(self.userData.data['role'], 'User')
      self.assertEqual(self.userData.data['username'], 'mirriam')

    def test_signup(self):
      self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.adminData.data['token'])
      response = self.client.post(self.postUserURI, self.validPostUserdata, format='json')
      self.assertEqual(response.status_code, 201)
      self.assertEqual(response.data['message'], 'User created successfully')
      self.assertEqual(response.data['data']['username'], 'testUsername')
      self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.adminData.data['token'])
      error = self.client.post(self.postUserURI, self.invalidPostUserdata, format='json')
      self.assertEqual(error.status_code, 400)
      self.assertEqual(error.data['username'], ['This field is required.'])

    def test_djangoNativeGet(self):
      response = self.client.get(self.djangoGetAllURI)
      self.assertEqual(response.status_code, 200)

    def test_listUser(self):
      self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.adminData.data['token'])
      response = self.client.get(self.listUserURI)
      self.assertEqual(response.status_code, 200)

    def test_listAllUser(self):
      self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.adminData.data['token'])
      response = self.client.get(self.listAllUserURI)
      self.assertEqual(response.status_code, 200)

    def test_updateUser(self):
      self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.adminData.data['token'])
      response = self.client.put(self.updateUserURI, self.validUserUpdateData, format='json')
      self.assertEqual(response.status_code, 201)

    def test_partialUpdateUser(self):
      self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.adminData.data['token'])
      response = self.client.patch(self.partialUpdateUserURI, self.validUserUpdateData, format='json')
      self.assertEqual(response.status_code, 201)

    def test_deleteUser(self):
      self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.adminData.data['token'])
      response = self.client.delete(self.deleteUserURI)
      self.assertEqual(response.status_code, 200)
