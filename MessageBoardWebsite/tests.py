from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="shehta")

    def test_post(self):
        self.assertEqual(self.post.text, "shehta")

    def test_post_correct_name(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code,200)

    def test_post_correct_location(self):
        response = self.client.get("MessageBoard/")

    def test_post_content(self):
        response = self.client.get(reverse('posts'))
        self.assertContains(response,"shehta")