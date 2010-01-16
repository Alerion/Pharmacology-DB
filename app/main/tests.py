from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse

class SomeTestCase(TestCase):
    fixtures = ['fixture.json']
    
    def setUp(self):
        self.client = Client()
        
    
    def test_func(self):
            
        data = {
            'pk': '1',
                    
        }
        url = reverse("main:drug_info")
        response = self.client.post(url, data)
        self.failUnlessEqual(response.status_code, 200)
            
        data = {
            'pks': ['1', '2', '3'],
            'pk': '1',
                    
        }
        url = reverse("main:load_drug_grid")
        response = self.client.post(url, data)
        self.failUnlessEqual(response.status_code, 200)
            
        data = {
            'pk': '3',
                    
        }
        url = reverse("main:drug_info")
        response = self.client.post(url, data)
        self.failUnlessEqual(response.status_code, 200)
            
        data = {
            'pks': ['1', '2', '3'],
            'pk': '3',
                    
        }
        url = reverse("main:load_drug_grid")
        response = self.client.post(url, data)
        self.failUnlessEqual(response.status_code, 200)
            
        url = reverse("main:index")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
            
        url = reverse("main:urls")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
            
        url = reverse("main:drug_edit_cm")
        response = self.client.get(url)
        self.failUnlessEqual(response.status_code, 200)
            
        data = {
            'node': 'root',
                    
        }
        url = reverse("main:drugs_tree")
        response = self.client.post(url, data)
        self.failUnlessEqual(response.status_code, 200)