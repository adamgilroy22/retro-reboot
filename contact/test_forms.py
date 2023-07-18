from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    """
    Test if post form is left blank when submitted
    """
    def test_name_is_required(self):
        form = ContactForm({'name': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_slug_is_required(self):
        form = ContactForm({'email': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')

    def test_message_is_required(self):
        form = ContactForm({'message': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('message', form.errors.keys())
        self.assertEqual(form.errors['message'][0], 'This field is required.')
