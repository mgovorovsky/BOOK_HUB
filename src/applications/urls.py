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
from applications import views as views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from applications import views
from . import apiviews


router = routers.SimpleRouter()
router.register(r'order-api', apiviews.OrderViewSet)

app_name = "applications"
urlpatterns = [ 
    path('order/<int:pk>/', views.OrderDetail.as_view(), name = "order_detail"),
    path('order/update/<int:pk>/', views.OrderUpdate.as_view(), name = "order_update"),
    path('order/', views.OrderList.as_view(), name = "order_list"),
    path('order/create/', views.OrderCreate.as_view(), name = "order_create"),
    path('order/delete/<int:pk>/', views.OrderDelete.as_view(), name = "order_delete"),
    path('about-us/', views.AboutUs.as_view()),


]   + router.urls


if not settings.IS_PRODUCTION:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
