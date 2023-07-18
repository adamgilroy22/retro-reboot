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

    def test_contact_page(self):
        """
        Test if testuser can access contact page
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')

    def test_open_tickets_normal(self):
        """
        Test if testuser gets error page when trying to force
        open tickets url
        """
        self.client.login(username="test_user", password="test_password")
        response = self.client.get('/contact/open-tickets')
        self.assertEqual(response.status_code, 403)
        self.assertTemplateUsed(response, 'errors/403.html')
