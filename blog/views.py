from django.shortcuts import render
from blog.models import Post

# Create your views here.
def blog_home(request):
    allPosts = Post.objects.all()
    context = {"allPosts": allPosts}
    return render(request, 'blog/home.html', context=context)
  
def blog_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {"post": post}
    return render(request, 'blog/post.html', context)