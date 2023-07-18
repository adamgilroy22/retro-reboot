from django.test import TestCase


class TestViews(TestCase):
    def test_basket_view(self):
        """
        Test if testuser can access products page
        """
        response = self.client.get('/basket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
