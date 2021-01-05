from django.urls import path
from blog.views import blog_home, blog_post

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('<str:slug>', blog_post, name='blog_post'),
]