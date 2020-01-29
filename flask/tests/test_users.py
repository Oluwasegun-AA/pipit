from tests.testBase import TestBase
from tests.mockData import loginData, signupData

class TestThis(TestBase):
    
  def test_get_user(self):
    token = self.getToken('shegs', 'password')
    res = self.get('/api/v1/user/1cf63969-6250-452e-9ae0-fa1dceca4ba5', loginData, token)
    self.assertEqual(res['data']['username'], 'theo')
  
  # def test_get_all_users(self):
  #   token = self.getToken('shegs', 'password')
  #   res = self.get('/api/v1/users', loginData, token)
  #   self.assertEqual(res[0]['username'], 'kasule')
