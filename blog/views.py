from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib.auth.models import User
from blog.models import Post, BlogComment
from blog.templatetags import extras

# Create your views here.
def blog_home(request):
    allPosts = reversed(Post.objects.all())
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

def create_post(request):
    # print(request.META['REMOTE_ADDR'])
    if request.user.is_authenticated:
        print(request.user)
        try:
            if request.method == "POST":
                if request.POST['action'] == "create_post":
                    post_title = request.POST['title']
                    post_content = request.POST['editorText']
                    slug = post_title.lower().replace(' ', '-').replace('?', '').replace('#', '')
                    # user = User.objects.get(username=request.user)
                    # name = f"{user.first_name} {user.last_name}"
                    # print(f'{post_title}--{slug} by {name.title()}')

                    post = Post(title=post_title, author=request.user, content=post_content, slug=slug)
                    post.save()
                    return redirect('/blog')
                else:
                    # TO-DO -> Create the logic to save drafts for posts
                    pass
        except Exception as e:
            return HttpResponse(e)
        return render(request, 'blog/create_post.html')

    else:
        return HttpResponse("Permission Denied", status=403)