from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here.
class HomePageTestCase(SimpleTestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_correct(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'CompanyWebsite/home.html')

class AboutPageTestCase(SimpleTestCase):
    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_by_name(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_template_correct(self):
        response = self.client.get(reverse('about'))
        self.assertTemplateUsed(response, 'CompanyWebsite/about.html')