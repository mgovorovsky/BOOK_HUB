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
from django.urls import path, include
from directories import views as directories_views
from random_number import views as random_number_views




urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('directories/currency/<int:pk>/', directories_views.currency_detail),
    path('directories/currency/update/<int:pk>/', directories_views.currency_update),
    path('directories/currency/', directories_views.currency_list),
    path('directories/currency/create/', directories_views.currency_create),
    path('rand/', random_number_views.get_random)


]
