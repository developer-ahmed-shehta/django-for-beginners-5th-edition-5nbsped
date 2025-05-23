from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Post
from django.urls import reverse
# Create your tests here.

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create(
            username='testuser',
            email='ahmedshehta0123@gmial.com',
            password='123456'
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title='testtitle',
            body='testcontent',
        )

    def test_post(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.title, 'testtitle')
        self.assertEqual(post.body, 'testcontent')
        self.assertEqual(post.author, self.user)

        self.assertEqual(post.get_absolute_url(),"/Blog/post/1")

    def test_post_detailview(self):  # new
        response = self.client.get(reverse("post_detail",
                                           kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/")
        #self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        #self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "Blog/post_detail.html")


    def test_post_create(self):
        response = self.client.post(reverse("post_new"),
                                    {
                                        'title': 'testtitle',
                                        'body': 'testcontent',
                                        'author': self.user.id,
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'testtitle')
        self.assertEqual(Post.objects.last().body, 'testcontent')

    def test_post_update(self):
        response = self.client.post(reverse("post_update",args=[self.post.pk]),
                                    {
                                     "title": "testtitle",
                                     "body": "testcontent",
                                    })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'testtitle')
        self.assertEqual(Post.objects.last().body, 'testcontent')

    def test_post_delete(self):
        response = self.client.post(reverse("post_delete",args=[self.post.pk]),)
        self.assertEqual(response.status_code, 302)
        self.assertIsNone(Post.objects.last())
