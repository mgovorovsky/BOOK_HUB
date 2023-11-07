from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse

# Create your views here.

class MyLoginView(auth_views.LoginView):
    template_name = "accs/login.html"

class MyLogoutView(auth_views.LogoutView):
    template_name = "accs/logout.html"

class MyPasswordChangeView(auth_views.PasswordChangeView):
    template_name = "registration/password_change_form.html"

class MyPasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"

class MyPasswordResetView(auth_views.PasswordResetView):
    template_name = "registration/password_reset_form.html"

class MyPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"

class MyPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"

class MyPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = "registration/password_reset_complete.html"