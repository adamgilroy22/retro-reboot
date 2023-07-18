from django.test import TestCase
from .forms import DiscountForm


class TestDiscountForm(TestCase):
    """
    Test if discount form is left blank when submitted
    """
    def test_code_is_required(self):
        form = DiscountForm({'code': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('code', form.errors.keys())
        self.assertEqual(form.errors['code'][0], 'This field is required.')
