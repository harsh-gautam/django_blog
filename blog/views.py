from django.shortcuts import render, redirect, Http404
from blog.models import Post, BlogComment

# Create your views here.
def blog_home(request):
    allPosts = Post.objects.all()
    context = {"allPosts": allPosts}
    return render(request, 'blog/home.html', context=context)
  
def blog_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post)
    # print(comments)
    context = {"post": post, "comments": comments}
    return render(request, 'blog/post.html', context)

def post_comment(request):
    
    if request.method == "POST":
        comment = request.POST['comment']
        user = request.user
        post_id = request.POST['post_id']
        post = Post.objects.get(post_id=post_id)

        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()

        return redirect(f'/blog/{post.slug}')
    else:
        return Http404("PAGE NOT FOUND")
