from django.shortcuts import render, redirect, HttpResponse, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
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
    query = request.GET['keyword']
    if len(query) > 50:
        allPosts = Post.objects.none()
    else:
        posts_title = Post.objects.filter(title__icontains=query)
        posts_content = Post.objects.filter(content__icontains=query)
        posts_author = Post.objects.filter(author__icontains=query)

        allPosts = posts_title.union(posts_content).union(posts_author)

    context = {"allPosts": allPosts, "query": query}
    return render(request, "core/search.html", context)

def handleSignup(request):
    if request.method == "POST":
        # Get the post data
        name = request.POST['name'].lower()
        email = request.POST['email'].lower()
        username = request.POST['username']
        password = request.POST['password']
        
        name_splitted = name.split()
        if len(name_splitted) == 1:
            fname = name_splitted[0]
        elif len(name_splitted) == 2:
            fname, lname = name_splitted[0], name_splitted[1]
        elif len(name_splitted) > 2:
            fname, lname = name_splitted[0], name_splitted[-1]

        user = User.objects.create_user(username, email, password)
        user.first_name = fname
        user.last_name = lname
        user.save()

        messages.success(request, "Your account has been successfully created. You can login now.")
        return redirect("/")
    else:
        raise Http404("Page not found")

def handleLogin(request):
    if request.method == "POST":
        username = request.POST['loginUsername']
        password = request.POST['loginPass']
        current_url = request.POST['current_url']
        print(current_url)

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}! Your log in was successful.')
            return redirect(current_url)
        else:
            messages.error(request, 'Invalid Credential! Please try again.')
            return redirect(current_url)
    else:
        return Http404("Page Not Found")

def handleLogout(request):
    logout(request)
    messages.warning(request, 'Logged out successfully')

    return redirect('/')