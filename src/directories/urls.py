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
# для bookname, genre, author сделаны постоянные ссылки в html

urlpatterns = [ 

    path('currency/<int:pk>/', views.CurrencyDetail.as_view(), name="currency_detail"),
    path('currency/update/<int:pk>/', views.CurrencyUpdate.as_view(), name="currency_update"),
    path('currency/', views.CurrencyList.as_view(), name="currency_list"),
    path('currency/create/', views.CurrencyCreate.as_view, name="currency_create"),
    path('currency/delete/<int:pk>/', views.CurrencyDelete.as_view(), name="currency_delete"),

    path('author/<int:pk>/', views.AuthorDetail.as_view(), name="author_detail"),
    path('author/update/<int:pk>/', views.AuthorUpdate.as_view(), name="author_update"),
    path('author/', views.AuthorList.as_view(), name="author_list"),
    path('author/create/', views.AuthorCreate.as_view(), name="author_create"),
    path('author/delete/<int:pk>/', views.AuthorDelete.as_view(), name="author_delete"),

    path('series/<int:pk>/', views.SeriesDetail.as_view(), name="series_detail"),
    path('series/update/<int:pk>/', views.SeriesUpdate.as_view(), name="series_update"),
    path('series/', views.SeriesList.as_view(), name="series_list"),
    path('series/create/', views.SeriesCreate.as_view(), name="series_create"),
    path('series/delete/<int:pk>/', views.SeriesDelete.as_view(), name="series_delete"),

    path('bookname/<int:pk>/', views.BookNameDetail.as_view(), name="bookname_detail"),
    path('bookname/update/<int:pk>/', views.BookNameUpdate.as_view(), name="bookname_update"),
    path('bookname/', views.BookNameList.as_view(), name="bookname_list"),
    path('bookname/create/', views.BookNameCreate.as_view(), name="bookname_create"),
    path('bookname/delete/<int:pk>/', views.BookNameDelete.as_view(), name="bookname_delete"),

    path('booktype/<int:pk>/', views.BookTypeDetail.as_view(), name="booktype_detail"),
    path('booktype/update/<int:pk>/', views.BookTypeUpdate.as_view(), name="booktype_update"),
    path('booktype/', views.BookTypeList.as_view(), name="booktype_list"),
    path('booktype/create/', views.BookTypeCreate.as_view(), name="booktype_create"),
    path('booktype/delete/<int:pk>/', views.BookTypeDelete.as_view(), name="booktype_delete"),


    path('rating/<int:pk>/', views.RatingDetail.as_view(), name="rating_detail"),
    path('rating/update/<int:pk>/', views.RatingUpdate.as_view(), name="rating_update"),
    path('rating/', views.RatingList.as_view(), name="rating_list"),
    path('rating/create/', views.RatingCreate.as_view(), name="rating_create"),
    path('rating/delete/<int:pk>/', views.RatingDelete.as_view(), name="rating_delete"),

    path('agelimit/<int:pk>/', views.AgeLimitDetail.as_view(), name="agelimit_detail"),
    path('agelimit/update/<int:pk>/', views.AgeLimitUpdate.as_view(), name="agelimit_update"),
    path('agelimit/', views.AgeLimitList.as_view(), name="agelimit_list"),
    path('agelimit/create/', views.AgeLimitCreate.as_view(), name="agelimit_create"),
    path('agelimit/delete/<int:pk>/', views.AgeLimitDelete.as_view(), name="agelimit_delete"),

    path('genre/<int:pk>/', views.GenreDetail.as_view(), name="genre_detail"),
    path('genre/update/<int:pk>/', views.GenreUpdate.as_view(), name="genre_update"),
    path('genre/', views.GenreList.as_view(), name="genre_list"),
    path('genre/create/', views.GenreCreate.as_view(), name="genre_create"),
    path('genre/delete/<int:pk>/', views.GenreDelete.as_view(), name="genre_delete"),
    
    path('copyrightholder/<int:pk>/', views.CopyrightHolderDetail.as_view(), name="copyrightholder_detail"),
    path('copyrightholder/update/<int:pk>/', views.CopyrightHolderUpdate.as_view(), name="copyrightholder_update"),
    path('copyrightholder/', views.CopyrightHolderList.as_view(), name="copyrightholder_list"),
    path('copyrightholder/create/', views.CopyrightHolderCreate.as_view(), name="copyrightholder_create"),
    path('copyrightholder/delete/<int:pk>/', views.CopyrightHolderDelete.as_view(), name="copyrightholder_delete"),
    
    #path('search', views.Search.as_view(), name="search"),
    
    ] 

if not settings.IS_PRODUCTION:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
