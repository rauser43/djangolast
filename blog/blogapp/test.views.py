from django.test import Client
from django.test import TestCase
from faker import Faker
from usersapp.models import BlogUser

class ViewsTest(TestCase):
    def SetUp(self):
        self.client = Client()
        self.fake = Faker

    def test_statuses(self):
        response= self.Client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.Client.get('/contact/')
        self.assertEqual(response.status_code, 200)

        name = form.cleaned_data['name']
        massage= form.cleaned_data['message']
        email =form.cleaned_data['email']

        response = self.client.post('/contact/', {'name': self.fake.name(), 'message':self.fake.text(),
                                                  'email': self.fake.email()})
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/')
        self.assertTrue('posts' in response.context)
        response.context['name']

        def test_login_required(self):
            BlogUser.objects.create_user(username="test_user", email="test@test.com", password="leo1234567")
            response = self.Client.get('/create/')
            self.assertEqual(response.status_code, 302)

           self.client.login(username='test_user', password="leo1234567")
            response = self.Client.get('/create/')
            self.assertEqual(response.status_code, 200)

