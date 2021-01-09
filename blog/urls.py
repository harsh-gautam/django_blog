from django.urls import path
from blog.views import blog_home, blog_post, create_post, post_comment

urlpatterns = [
    # APIs
    path('post_comment', post_comment, name='post_comment'),

    path('', blog_home, name='blog_home'),
    path('create', create_post, name='create_post'),
    path('<str:slug>', blog_post, name='blog_post'),
    
]