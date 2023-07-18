from django.test import TestCase, Client
from django.urls import reverse
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

        """
        Get correct urls for product list
        """
        self.client = Client()
        self.product_list_url = reverse('products')

    def test_product_list(self):
        """
        Test if testuser can access products page
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get(self.product_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_add_product_normal(self):
        """
        Test if testuser gets redirected to homepage when
        trying to add a product as non admin
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/products/add')
        self.assertEqual(response.status_code, 301)

    def test_edit_product_normal(self):
        """
        Test if testuser gets redirected to homepage when
        trying to edit a product as non admin
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/products/edit/1')
        self.assertEqual(response.status_code, 301)

    def test_delete_product_normal(self):
        """
        Test if testuser gets redirected to homepage when
        trying to delete a product as non admin
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/products/delete/1')
        self.assertEqual(response.status_code, 301)
