"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = "accs"

urlpatterns = [ 
    path("login/", views.MyLoginView.as_view(), name="login"),
    path("logout/", views.MyLogoutView.as_view(), name="logout"),
    path("pass_change/", views.MyPasswordChangeView.as_view(), name="pass_change"),
    path("pass_change_done/", views.MyPasswordChangeDoneView.as_view(), name="pass_change_done"),
    path("pass_reset/", views.MyPasswordResetView.as_view(), name="pass_reset"),
    path("pass_reset_done/", views.MyPasswordResetDoneView.as_view(), name="pass_reset_done"),
    path("pass_reset_confirm/", views.MyPasswordResetConfirmView.as_view(), name="pass_reset_confirm"),
    path("pass_reset_complete/", views.MyPasswordResetCompleteView.as_view(), name="pass_reset_complete"),



] 

if not settings.IS_PRODUCTION:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
