from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This website home")

def contact(request):
    return HttpResponse("This contact")

def about(request):
    return HttpResponse("This about")