from django.test import TestCase
from .forms import ProductForm


class TestProductForm(TestCase):
    """
    Test if product form is left blank when submitted
    """

    def test_name_is_required(self):
        form = ProductForm({'name': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_year_is_required(self):
        form = ProductForm({'year': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('year', form.errors.keys())
        self.assertEqual(form.errors['year'][0], 'This field is required.')

    def test_description_is_required(self):
        form = ProductForm({'description': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description']
                         [0], 'This field is required.')

    def test_price_is_required(self):
        form = ProductForm({'price': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')

    def test_stock_is_required(self):
        form = ProductForm({'stock': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('stock', form.errors.keys())
        self.assertEqual(form.errors['stock'][0], 'This field is required.')
