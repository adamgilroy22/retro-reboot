from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('post/add/', views.add_post, name='add_post'),
    path('post/edit/<slug:slug>/', views.edit_post, name='edit_post'),
    path('post/delete/<slug:slug>/', views.delete_post, name='delete_post'),
]
