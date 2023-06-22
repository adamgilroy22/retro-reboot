from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(published=True).order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 6
