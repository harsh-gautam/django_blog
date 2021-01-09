from django.urls import path
from core.views import home, contact, about, search, handleSignup, handleLogin, handleLogout

urlpatterns = [
    path('', home, name="Home"),
    path('about', about, name="About"),
    path('contact', contact, name="Contact"),
    path('search', search, name="Search"),

    # APIs
    path('signup', handleSignup, name="Signup"),
    path('login', handleLogin, name="Login"),
    path('logout', handleLogout, name="Logout"),
]