from django.shortcuts import render, redirect, Http404
from blog.models import Post, BlogComment
from blog.templatetags import extras

# Create your views here.
def blog_home(request):
    allPosts = Post.objects.all()
    context = {"allPosts": allPosts}
    return render(request, 'blog/home.html', context=context)
  
def blog_post(request, slug):
    post = Post.objects.filter(slug=slug).first()
    comments = BlogComment.objects.filter(post=post, parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replyDict = {}
    for reply in replies:
        if reply.parent.com_id not in replyDict.keys():
            replyDict[reply.parent.com_id] = [reply]
        else:
            replyDict[reply.parent.com_id].append(reply)
    # print(replyDict)
    context = {"post": post, "comments": comments, "replyDict": replyDict}
    return render(request, 'blog/post.html', context)

def post_comment(request):
    
    if request.method == "POST":
        comment = request.POST['comment']
        user = request.user
        post_id = request.POST['post_id']
        post = Post.objects.get(post_id=post_id)

        parentComId = request.POST['parentComId']

        if parentComId == "":
            
            comment = BlogComment(comment=comment, user=user, post=post)
        else:
            parent = BlogComment.objects.get(com_id=parentComId)
            comment = BlogComment(comment=comment, user=user, post=post, parent=parent)
        comment.save()

        return redirect(f'/blog/{post.slug}')
    else:
        return Http404("PAGE NOT FOUND")
