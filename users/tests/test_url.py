from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import user_create, auth, deauth, index, try_reg, try_auth
class TestUrls(SimpleTestCase):

    def test_Reg_url_is_resolves(self):
        url = reverse('Reg')
        print(resolve(url))
        self.assertEquals(resolve(url).func, user_create)
    
    def test_Auth_url_is_resolves(self):
        url = reverse('Auth')
        print(resolve(url))
        self.assertEquals(resolve(url).func, auth) 
    
    def test_DeAuth_url_is_resolves(self):
        url = reverse('DeAuth')
        print(resolve(url))
        self.assertEquals(resolve(url).func, deauth)
    
    def test_index_url_is_resolves(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)
    
    def test_tryReg_url_is_resolves(self):
        url = reverse('tryReg')
        print(resolve(url))
        self.assertEquals(resolve(url).func, try_reg)
    
    def test_Reg_url_is_resolves(self):
        url = reverse('tryAuth')
        print(resolve(url))
        self.assertEquals(resolve(url).func, try_auth)
    
        
    