from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from . import models, forms
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

User = get_user_model()


class CurrencyCreate(generic.CreateView):
    template_name="directories/currency_create.html"
    model = models.Currency
    form_class = forms.CurrencyModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CurrencyUpdate(generic.UpdateView):
    template_name="directories/currency_update.html"
    model = models.Currency
    form_class = forms.CurrencyModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CurrencyDetail(generic.DetailView):
    template_name="directories/currency_detail.html"
    model = models.Currency
    login_url = "admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CurrencyDelete(generic.DeleteView):
    template_name="directories/currency_delete.html"
    model = models.Currency
    success_url = "/directories/currency/" 

class CurrencyList(generic.ListView):
    template_name="directories/currency_list.html"
    model = models.Currency

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
# Author author
class AuthorCreate(generic.CreateView):
    template_name="directories/author_create.html"
    model = models.Author
    form_class = forms.AuthorModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AuthorUpdate(generic.UpdateView):
    template_name="directories/author_update.html"
    model = models.Author
    form_class = forms.AuthorModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AuthorDetail(generic.DetailView):
    template_name="directories/author_detail.html"
    model = models.Author

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AuthorDelete(generic.DeleteView):
    template_name="directories/author_delete.html"
    model = models.Author
    success_url = "/directories/author/" 

class AuthorList(generic.ListView):
    template_name="directories/author_list.html"
    model = models.Author

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
# Series series
class SeriesCreate(generic.CreateView):
    template_name="directories/series_create.html"
    model = models.Series
    form_class = forms.SeriesModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class SeriesUpdate(generic.UpdateView):
    template_name="directories/series_update.html"
    model = models.Series
    form_class = forms.SeriesModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class SeriesDetail(generic.DetailView):
    template_name="directories/series_detail.html"
    model = models.Series

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class SeriesDelete(generic.DeleteView):
    template_name="directories/series_delete.html"
    model = models.Series
    success_url = "/directories/series/" 

class SeriesList(generic.ListView):
    template_name="directories/series_list.html"
    model = models.Series

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    

# BookName bookname
class BookNameCreate(generic.CreateView):
    template_name="directories/bookname_create.html"
    model = models.BookName
    form_class = forms.BookNameModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookNameUpdate(generic.UpdateView):
    template_name="directories/bookname_update.html"
    model = models.BookName
    form_class = forms.BookNameModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookNameDetail(generic.DetailView):
    template_name="directories/bookname_detail.html"
    model = models.BookName

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookNameDelete(generic.DeleteView):
    template_name="directories/bookname_delete.html"
    model = models.BookName
    success_url = "/directories/bookname/" 

class BookNameList(generic.ListView):
    template_name="directories/bookname_list.html"
    model = models.BookName

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
# Rating rating
class RatingCreate(generic.CreateView):
    template_name="directories/rating_create.html"
    model = models.Rating
    form_class = forms.RatingModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class RatingUpdate(generic.UpdateView):
    template_name="directories/rating_update.html"
    model = models.Rating
    form_class = forms.RatingModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class RatingDetail(generic.DetailView):
    template_name="directories/rating_detail.html"
    model = models.Rating

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class RatingDelete(generic.DeleteView):
    template_name="directories/rating_delete.html"
    model = models.Rating
    success_url = "/directories/rating/" 

class RatingList(generic.ListView):
    template_name="directories/rating_list.html"
    model = models.Rating

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
# AgeLimit agelimit
class AgeLimitCreate(generic.CreateView):
    template_name="directories/agelimit_create.html"
    model = models.AgeLimit
    form_class = forms.AgeLimitModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AgeLimitUpdate(generic.UpdateView):
    template_name="directories/agelimit_update.html"
    model = models.AgeLimit
    form_class = forms.AgeLimitModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AgeLimitDetail(generic.DetailView):
    template_name="directories/agelimit_detail.html"
    model = models.AgeLimit

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AgeLimitDelete(generic.DeleteView):
    template_name="directories/agelimit_delete.html"
    model = models.AgeLimit
    success_url = "/directories/ageLimit/" 

class AgeLimitList(generic.ListView):
    template_name="directories/agelimit_list.html"
    model = models.AgeLimit

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context

#BookType booktype 
class BookTypeCreate(generic.CreateView):
    template_name="directories/booktype_create.html"
    model = models.BookType
    form_class = forms.BookTypeModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookTypeUpdate(generic.UpdateView):
    template_name="directories/booktype_update.html"
    model = models.BookType
    form_class = forms.BookTypeModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookTypeDetail(generic.DetailView):
    template_name="directories/booktype_detail.html"
    model = models.BookType

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookTypeDelete(generic.DeleteView):
    template_name="directories/booktype_delete.html"
    model = models.BookType
    success_url = "/directories/booktype/" 

class BookTypeList(generic.ListView):
    template_name="directories/booktype_list.html"
    model = models.BookType

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context



# Genre genre 
class GenreCreate(generic.CreateView):
    template_name="directories/genre_create.html"
    model = models.Genre
    form_class = forms.GenreModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class GenreUpdate(generic.UpdateView):
    template_name="directories/genre_update.html"
    model = models.Genre
    form_class = forms.GenreModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class GenreDetail(generic.DetailView):
    template_name="directories/genre_detail.html"
    model = models.Genre

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class GenreDelete(generic.DeleteView):
    template_name="directories/genre_delete.html"
    model = models.Genre
    success_url = "/directories/genre/" 

class GenreList(generic.ListView):
    template_name="directories/genre_list.html"
    model = models.Genre

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
 
# CopyrightHolder
class CopyrightHolderCreate(generic.CreateView):
    template_name="directories/copyrightholder_create.html"
    model = models.CopyrightHolder
    form_class = forms.CopyrightHolderModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CopyrightHolderUpdate(generic.UpdateView):
    template_name="directories/copyrightholder_update.html"
    model = models.CopyrightHolder
    form_class = forms.CopyrightHolderModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CopyrightHolderDetail(generic.DetailView):
    template_name="directories/copyrightholder_detail.html"
    model = models.CopyrightHolder

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CopyrightHolderDelete(generic.DeleteView):
    template_name="directories/copyrightholder_delete.html"
    model = models.CopyrightHolder
    success_url = "/directories/copyrightholder/" 

class CopyrightHolderList(generic.ListView):
    template_name="directories/copyrightholder_list.html"
    model = models.CopyrightHolder

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    


def book_types(request):
    object = models.BookType.objects
    author = models.BookName.author
    genre = models.BookName.genre
    price = models.BookName.price
    rating = models.BookName.rating

    return render(
        request, 
        template_name="directories/booktype_main.html",
        context={"object": object, "author": author, "genre": genre, "price": price, "rating": rating}
    )

# def currency_detail(request, pk):
#    # directories/currency/
#     obj = models.Currency.objects.get(pk=pk)
#     context = {"obj" : obj, "verb": "detail"}
#     return render(
#         request, 
#         template_name="directories/currency_detail.html",
#         context=context
#     )

# def currency_list(request):
#     obj_list = models.Currency.objects.all()
#     context = {"object_list" : obj_list, "verb": "list"}
#     return render(
#         request, 
#         template_name="directories/currency_list.html",
#         context=context
#     )

# делаем модельную форму (CurrencyModelForm - которая берет данные из класса,
# а не из отдельной для каждого класса, еще раз описывающей поля)
# def currency_create(request):
#     template_name="directories/currency_create.html"
#     if request.method == "GET":
#         form = forms.CurrencyModelForm()
#         context = {"verb": "create", "form": form}
#     elif request.method == "POST":
#         form = forms.CurrencyModelForm(request.POST)
#         if form.is_valid():
#             obj = form.save()
#             print(form.instance.pk)
#             return HttpResponseRedirect(f"/directories/currency/{obj.pk}")
#         else: 
#             context = {"verb": "create", "form": form}

#     else:
#         raise Exception ("Wrong method")
#     return render(
#             request, 
#             template_name=template_name,
#             context=context,
#     )    

# def currency_update(request, pk):
#     if request.method == "GET":
#         template_name="directories/currency_update.html",
#         obj = models.Currency.objects.get(pk=pk)
#         form = forms.CurrencyForm({
#             "name": obj.name,
#             "description": obj.description,
#         })
#         context = {"obj" : obj, "verb": "Update", "form": form}

#     elif request.method == "POST":
#         form = forms.CurrencyForm(request.POST)
#         if form.is_valid():
#             form.update_obj(pk)
#             return HttpResponseRedirect(f"/directories/currency/{pk}")    

#     else:
#         raise Exception ("Wrong method")
#     return render(
#         request, 
#         template_name=template_name,
#         context=context
#     )   