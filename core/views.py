from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import ContactForm
from blog.models import Post
# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def contact(request):
    
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        query = request.POST["query"]

        contact = ContactForm(name=name, email=email, query=query)
        contact.save()
        messages.success(request, "Your query has been send to our team.")
        return redirect('/contact')

    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def search(request):
    query = request.GET['search']
    if len(query) > 50:
        allPosts = Post.objects.none()
    else:
        posts_title = Post.objects.filter(title__icontains=query)
        posts_content = Post.objects.filter(content__icontains=query)
        posts_author = Post.objects.filter(author__icontains=query)

        allPosts = posts_title.union(posts_content).union(posts_author)

    context = {"allPosts": allPosts, "query": query}
    return render(request, "core/search.html", context)