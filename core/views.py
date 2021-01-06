from django.shortcuts import render, redirect
from core.models import ContactForm

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
        # print(name, email, query)
        return redirect('/contact')

    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')