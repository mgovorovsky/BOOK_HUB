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
from applications import views as applications_views
from random_number import views as random_number_views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [ 
    path('admin/', admin.site.urls),

    path('directories/currency/<int:pk>/', directories_views.CurrencyDetail.as_view()),
    path('directories/currency/update/<int:pk>/', directories_views.CurrencyUpdate.as_view()),
    path('directories/currency/', directories_views.CurrencyList.as_view()),
    path('directories/currency/create/', directories_views.CurrencyCreate.as_view()),
    path('directories/currency/delete/<int:pk>/', directories_views.CurrencyDelete.as_view()),

    path('directories/author/<int:pk>/', directories_views.AuthorDetail.as_view()),
    path('directories/author/update/<int:pk>/', directories_views.AuthorUpdate.as_view()),
    path('directories/author/', directories_views.AuthorList.as_view()),
    path('directories/author/create/', directories_views.AuthorCreate.as_view()),
    path('directories/author/delete/<int:pk>/', directories_views.AuthorDelete.as_view()),

    path('directories/series/<int:pk>/', directories_views.SeriesDetail.as_view()),
    path('directories/series/update/<int:pk>/', directories_views.SeriesUpdate.as_view()),
    path('directories/series/', directories_views.SeriesList.as_view()),
    path('directories/series/create/', directories_views.SeriesCreate.as_view()),
    path('directories/series/delete/<int:pk>/', directories_views.SeriesDelete.as_view()),

    path('directories/bookname/<int:pk>/', directories_views.BookNameDetail.as_view()),
    path('directories/bookname/update/<int:pk>/', directories_views.BookNameUpdate.as_view()),
    path('directories/bookname/', directories_views.BookNameList.as_view()),
    path('directories/bookname/create/', directories_views.BookNameCreate.as_view()),
    path('directories/bookname/delete/<int:pk>/', directories_views.BookNameDelete.as_view()),

    path('directories/booktype/<int:pk>/', directories_views.BookTypeDetail.as_view()),
    path('directories/booktype/update/<int:pk>/', directories_views.BookTypeUpdate.as_view()),
    path('directories/booktype/', directories_views.BookTypeList.as_view()),
    path('directories/booktype/create/', directories_views.BookTypeCreate.as_view()),
    path('directories/booktype/delete/<int:pk>/', directories_views.BookTypeDelete.as_view()),

    path('directories/rating/<int:pk>/', directories_views.RatingDetail.as_view()),
    path('directories/rating/update/<int:pk>/', directories_views.RatingUpdate.as_view()),
    path('directories/rating/', directories_views.RatingList.as_view()),
    path('directories/rating/create/', directories_views.RatingCreate.as_view()),
    path('directories/rating/delete/<int:pk>/', directories_views.RatingDelete.as_view()),

    path('directories/agelimit/<int:pk>/', directories_views.AgeLimitDetail.as_view()),
    path('directories/agelimit/update/<int:pk>/', directories_views.AgeLimitUpdate.as_view()),
    path('directories/agelimit/', directories_views.AgeLimitList.as_view()),
    path('directories/agelimit/create/', directories_views.AgeLimitCreate.as_view()),
    path('directories/agelimit/delete/<int:pk>/', directories_views.AgeLimitDelete.as_view()),

    path('directories/genre/<int:pk>/', directories_views.GenreDetail.as_view()),
    path('directories/genre/update/<int:pk>/', directories_views.GenreUpdate.as_view()),
    path('directories/genre/', directories_views.GenreList.as_view()),
    path('directories/genre/create/', directories_views.GenreCreate.as_view()),
    path('directories/genre/delete/<int:pk>/', directories_views.GenreDelete.as_view()),

    path('directories/copyrightholder/<int:pk>/', directories_views.CopyrightHolderDetail.as_view()),
    path('directories/copyrightholder/update/<int:pk>/', directories_views.CopyrightHolderUpdate.as_view()),
    path('directories/copyrightholder/', directories_views.CopyrightHolderList.as_view()),
    path('directories/copyrightholder/create/', directories_views.CopyrightHolderCreate.as_view()),
    path('directories/copyrightholder/delete/<int:pk>/', directories_views.CopyrightHolderDelete.as_view()),

    path('applications/order/<int:pk>/', applications_views.OrderDetail.as_view()),
    path('applications/order/update/<int:pk>/', applications_views.OrderUpdate.as_view()),
    path('applications/order/', applications_views.OrderList.as_view()),
    path('applications/order/create/', applications_views.OrderCreate.as_view()),
    path('applications/order/delete/<int:pk>/', applications_views.OrderDelete.as_view()),
    path('about-us/', applications_views.AboutUs.as_view()),

    path('rand/', random_number_views.get_random)


] 
if not settings.IS_PRODUCTION:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
