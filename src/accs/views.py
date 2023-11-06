from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Create your views here.


class MyLoginView(auth_views.LoginView):
    template_name = "accs/login.html"

class MyLogoutView(auth_views.LogoutView):
    template_name = "accs/logout.html"