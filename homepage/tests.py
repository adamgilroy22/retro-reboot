from django.test import TestCase


class TestViews(TestCase):
    def test_profile(self):
        """
        Test if homepage loads
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'homepage/index.html')
