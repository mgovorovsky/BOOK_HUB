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
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "directories"

urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('currency/<int:pk>/', views.CurrencyDetail.as_view(), name="currency_detail"),
    path('currency/update/<int:pk>/', views.CurrencyUpdate.as_view(), name="currency_update"),
    path('currency/', views.CurrencyList.as_view(), name="currency_update"),
    path('currency/create/', views.CurrencyCreate.as_view, name="currency_create"),
    path('currency/delete/<int:pk>/', views.CurrencyDelete.as_view(), name="currency_delete"),

    path('author/<int:pk>/', views.AuthorDetail.as_view(), name="author_detail"),
    path('author/update/<int:pk>/', views.AuthorUpdate.as_view(), name="author_update"),
    path('author/', views.AuthorList.as_view(), name="author_list"),
    path('author/create/', views.AuthorCreate.as_view(), name="author_create"),
    path('author/delete/<int:pk>/', views.AuthorDelete.as_view(), name="author_delete"),

    path('series/<int:pk>/', views.SeriesDetail.as_view()),
    path('series/update/<int:pk>/', views.SeriesUpdate.as_view()),
    path('series/', views.SeriesList.as_view()),
    path('series/create/', views.SeriesCreate.as_view()),
    path('series/delete/<int:pk>/', views.SeriesDelete.as_view()),

    path('bookname/<int:pk>/', views.BookNameDetail.as_view()),
    path('bookname/update/<int:pk>/', views.BookNameUpdate.as_view()),
    path('bookname/', views.BookNameList.as_view()),
    path('bookname/create/', views.BookNameCreate.as_view()),
    path('bookname/delete/<int:pk>/', views.BookNameDelete.as_view()),

    path('booktype/<int:pk>/', views.BookTypeDetail.as_view()),
    path('booktype/update/<int:pk>/', views.BookTypeUpdate.as_view()),
    path('booktype/', views.BookTypeList.as_view()),
    path('booktype/create/', views.BookTypeCreate.as_view()),
    path('booktype/delete/<int:pk>/', views.BookTypeDelete.as_view()),


    path('rating/<int:pk>/', views.RatingDetail.as_view()),
    path('rating/update/<int:pk>/', views.RatingUpdate.as_view()),
    path('rating/', views.RatingList.as_view()),
    path('rating/create/', views.RatingCreate.as_view()),
    path('rating/delete/<int:pk>/', views.RatingDelete.as_view()),

    path('agelimit/<int:pk>/', views.AgeLimitDetail.as_view()),
    path('agelimit/update/<int:pk>/', views.AgeLimitUpdate.as_view()),
    path('agelimit/', views.AgeLimitList.as_view()),
    path('agelimit/create/', views.AgeLimitCreate.as_view()),
    path('agelimit/delete/<int:pk>/', views.AgeLimitDelete.as_view()),

    path('genre/<int:pk>/', views.GenreDetail.as_view()),
    path('genre/update/<int:pk>/', views.GenreUpdate.as_view()),
    path('genre/', views.GenreList.as_view()),
    path('genre/create/', views.GenreCreate.as_view()),
    path('genre/delete/<int:pk>/', views.GenreDelete.as_view()),
    path('copyrightholder/update/<int:pk>/', views.CopyrightHolderUpdate.as_view()),
    path('copyrightholder/', views.CopyrightHolderList.as_view()),
    path('copyrightholder/create/', views.CopyrightHolderCreate.as_view()),
    path('copyrightholder/delete/<int:pk>/', views.CopyrightHolderDelete.as_view()),
    
    
    ] 

if not settings.IS_PRODUCTION:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
