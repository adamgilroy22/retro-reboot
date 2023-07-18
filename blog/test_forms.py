from django.test import TestCase
from .forms import PostForm, CommentForm


class TestPostForm(TestCase):
    """
    Test if post form is left blank when submitted
    """
    def test_title_is_required(self):
        form = PostForm({'title': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_slug_is_required(self):
        form = PostForm({'slug': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('slug', form.errors.keys())
        self.assertEqual(form.errors['slug'][0], 'This field is required.')

    def test_content_is_required(self):
        form = PostForm({'content': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('content', form.errors.keys())
        self.assertEqual(form.errors['content'][0], 'This field is required.')

    def test_excerpt_is_required(self):
        form = PostForm({'excerpt': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('excerpt', form.errors.keys())
        self.assertEqual(form.errors['excerpt'][0], 'This field is required.')


class TestCommentForm(TestCase):
    """
    Test if post form is left blank when submitted
    """
    def test_comment_is_required(self):
        form = CommentForm({'body': ""})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')
