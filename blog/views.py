from django.shortcuts import render, HttpResponse

# Create your views here.
def blog_home(request):
    return HttpResponse("This is blog home")
  
def blog_post(request, slug):
    return HttpResponse("This is blog post - "+slug)