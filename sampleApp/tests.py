from django.test import  SimpleTestCase

# Create your tests here.
class HomePageTestCase(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class AboutPageTestCase(SimpleTestCase):
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)