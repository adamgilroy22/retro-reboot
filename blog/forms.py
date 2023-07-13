from .models import Comment, Post
from products.widgets import CustomClearableFileInput
from django_summernote.widgets import SummernoteWidget
from django_summernote.fields import SummernoteTextFormField
from django import forms


class PostForm(forms.ModelForm):
    """
    Create a new post using Post model
    """
    class Meta:
        model = Post
        fields = ('title', 'slug', 'content',
                  'excerpt', 'image', 'published',)

    content = forms.CharField(widget=SummernoteWidget())

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)


class CommentForm(forms.ModelForm):
    """
    Create a new comment using Comment model
    """
    class Meta:
        model = Comment
        fields = ('body',)
