from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        """
        Create testuser to test pages where
        you need to be logged in to view
        """
        testuser = User.objects.create_user(
            username="test_user",
            password="test_password",
            email="test@test.com"
        )
        testuser.save()

    def test_blog_list(self):
        """
        Test if testuser can access blog
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blog.html')

    def test_add_blog_normal(self):
        """
        Test if testuser gets redirected to homepage when
        trying to add a blog post as non admin
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/blog/post/add')
        self.assertEqual(response.status_code, 301)

    def test_edit_blog_normal(self):
        """
        Test if testuser gets redirected to homepage when
        trying to edit a blog post as non admin
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/blog/post/edit/test-post')
        self.assertEqual(response.status_code, 301)

    def test_delete_blog_normal(self):
        """
        Test if testuser gets redirected to homepage when
        trying to edit a blog post as non admin
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/blog/post/delete/test-post')
        self.assertEqual(response.status_code, 301)
