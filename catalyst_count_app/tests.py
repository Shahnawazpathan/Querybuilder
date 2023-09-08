
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import csv_data, user

class YourAppTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

    def test_csv_upload(self):
        with open('path_to_your_test_file.csv', 'rb') as file:
            response = self.client.post(reverse('csv_upload'), {'csv_file': file})
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CSV data uploaded successfully.")


    def test_user_login(self):
        response = self.client.post(reverse('user_login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 302)  
        self.assertRedirects(response, reverse('uploaddata'))

    
    def test_querybuilder(self):
        response = self.client.post(reverse('querybuilder'), {'company_data': 'TestCompany'})
        self.assertEqual(response.status_code, 302)  


        self.assertContains(response, "data record found.")


    def test_user_logout(self):
        response = self.client.get(reverse('user_logout'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Logged out successfully.")



    def tearDown(self):
        self.client.logout()

