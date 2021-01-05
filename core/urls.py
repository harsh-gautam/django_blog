from django.urls import path
from core.views import home, contact, about

urlpatterns = [
    path('', home, name="Home"),
    path('about', about, name="About"),
    path('contact', contact, name="Contact"),

]