from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import ContactForm
import json
import time
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