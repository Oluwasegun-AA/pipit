from tests.testBase import TestBase
from tests.mockData import loginData, signupData

class TestThis(TestBase):
    
  def test_Login(self):
    res = self.post('/api/v1/auth/login/', loginData)
    self.assertEqual(res['status'], 200)

  def test_signup(self):
    res = self.post('/api/v1/auth/signup/', signupData)
    self.assertEqual(res['status'], 200)
    self.assertEqual(res['data']['username'], 'testUsername')



