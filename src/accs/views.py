from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Create your views here.


class MyLoginView(auth_views.LoginView):
    template_name = "accs/login.html"