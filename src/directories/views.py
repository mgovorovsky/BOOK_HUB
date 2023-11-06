from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from . import models, forms
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

User = get_user_model()


class CurrencyCreate(LoginRequiredMixin, generic.CreateView):
    template_name="directories/currency_create.html"
    model = models.Currency
    login_url = "/admin/login/"
    form_class = forms.CurrencyModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
   
class CurrencyUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="directories/currency_update.html"
    model = models.Currency
    login_url = "/admin/login/"
    form_class = forms.CurrencyModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CurrencyDetail(LoginRequiredMixin, generic.DetailView):
    template_name="directories/currency_detail.html"
    model = models.Currency
    login_url = "/admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CurrencyDelete(LoginRequiredMixin, generic.DeleteView):
    template_name="directories/currency_delete.html"
    model = models.Currency
    login_url = "/admin/login/"
    success_url = "/directories/currency/" 

class CurrencyList(LoginRequiredMixin, generic.ListView):
    template_name="directories/currency_list.html"
    model = models.Currency

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
# Author author
class AuthorCreate(LoginRequiredMixin, generic.CreateView):
    template_name="directories/author_create.html"
    model = models.Author
    login_url = "/admin/login/"
    form_class = forms.AuthorModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AuthorUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="directories/author_update.html"
    model = models.Author
    login_url = "/admin/login/"
    form_class = forms.AuthorModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AuthorDetail(generic.DetailView):
    template_name="directories/author_detail.html"
    model = models.Author
    login_url = "/admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AuthorDelete(LoginRequiredMixin,generic.DeleteView):
    template_name="directories/author_delete.html"
    model = models.Author
    login_url = "/admin/login/"
    success_url = "/directories/author/" 

class AuthorList(generic.ListView):
    template_name="directories/author_list.html"
    model = models.Author
    login_url = "/admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
# Series series
class SeriesCreate(LoginRequiredMixin, generic.CreateView):
    template_name="directories/series_create.html"
    model = models.Series
    login_url = "/admin/login/"
    form_class = forms.SeriesModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class SeriesUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="directories/series_update.html"
    model = models.Series
    login_url = "/admin/login/"
    form_class = forms.SeriesModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class SeriesDetail(generic.DetailView):
    template_name="directories/series_detail.html"
    model = models.Series
    login_url = "/admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class SeriesDelete(LoginRequiredMixin, generic.DeleteView):
    template_name="directories/series_delete.html"
    model = models.Series
    login_url = "/admin/login/"
    success_url = "/directories/series/" 

class SeriesList(generic.ListView):
    template_name="directories/series_list.html"
    model = models.Series

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    

# BookName bookname
class BookNameCreate(LoginRequiredMixin, generic.CreateView):
    template_name="directories/bookname_create.html"
    model = models.BookName
    login_url = "/admin/login/"
    form_class = forms.BookNameModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookNameUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="directories/bookname_update.html"
    model = models.BookName
    login_url = "/admin/login/"
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
    
class BookNameDelete(LoginRequiredMixin, generic.DeleteView):
    template_name="directories/bookname_delete.html"
    model = models.BookName
    login_url = "/admin/login/"
    success_url = "/directories/bookname/" 

class BookNameList(generic.ListView):
    template_name="directories/bookname_list.html"
    login_url = "/admin/login/"
    model = models.BookName

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
# Rating rating
class RatingCreate(LoginRequiredMixin, generic.CreateView):
    template_name="directories/rating_create.html"
    model = models.Rating
    form_class = forms.RatingModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class RatingUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="directories/rating_update.html"
    model = models.Rating
    login_url = "/admin/login/"
    form_class = forms.RatingModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class RatingDetail(LoginRequiredMixin, generic.DetailView):
    template_name="directories/rating_detail.html"
    model = models.Rating
    login_url = "/admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class RatingDelete(LoginRequiredMixin, generic.DeleteView):
    template_name="directories/rating_delete.html"
    model = models.Rating
    login_url = "/admin/login/"
    success_url = "/directories/rating/" 

class RatingList(LoginRequiredMixin, generic.ListView):
    template_name="directories/rating_list.html"
    model = models.Rating

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
# AgeLimit agelimit
class AgeLimitCreate(LoginRequiredMixin, generic.CreateView):
    template_name="directories/agelimit_create.html"
    model = models.AgeLimit
    login_url = "/admin/login/"
    form_class = forms.AgeLimitModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AgeLimitUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="directories/agelimit_update.html"
    model = models.AgeLimit
    login_url = "/admin/login/"
    form_class = forms.AgeLimitModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AgeLimitDetail(LoginRequiredMixin, generic.DetailView):
    template_name="directories/agelimit_detail.html"
    model = models.AgeLimit
    login_url = "/admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class AgeLimitDelete(LoginRequiredMixin, generic.DeleteView):
    template_name="directories/agelimit_delete.html"
    model = models.AgeLimit
    login_url = "/admin/login/"
    success_url = "/directories/ageLimit/" 

class AgeLimitList(LoginRequiredMixin, generic.ListView):
    template_name="directories/agelimit_list.html"
    model = models.AgeLimit
    login_url = "/admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context

#BookType booktype 
class BookTypeCreate(LoginRequiredMixin, generic.CreateView):
    template_name="directories/booktype_create.html"
    model = models.BookType
    login_url = "/admin/login/"
    form_class = forms.BookTypeModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookTypeUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="directories/booktype_update.html"
    model = models.BookType
    login_url = "/admin/login/"
    form_class = forms.BookTypeModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookTypeDetail(LoginRequiredMixin, generic.DetailView):
    template_name="directories/booktype_detail.html"
    model = models.BookType
    login_url = "/admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class BookTypeDelete(LoginRequiredMixin, generic.DeleteView):
    template_name="directories/booktype_delete.html"
    model = models.BookType
    login_url = "/admin/login/"
    success_url = "/directories/booktype/" 

class BookTypeList(generic.ListView):
    template_name="directories/booktype_list.html"
    login_url = "/admin/login/"
    model = models.BookType

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context



# Genre genre 
# @login_required 
class GenreCreate(LoginRequiredMixin, generic.CreateView):
    template_name="directories/genre_create.html"
    model = models.Genre
    login_url = "/admin/login/"
    form_class = forms.GenreModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class GenreUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="directories/genre_update.html"
    model = models.Genre
    login_url = "/admin/login/"
    form_class = forms.GenreModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class GenreDetail(generic.DetailView):
    template_name="directories/genre_detail.html"
    login_url = "/admin/login/"
    model = models.Genre

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class GenreDelete(LoginRequiredMixin, generic.DeleteView):
    template_name="directories/genre_delete.html"
    model = models.Genre
    login_url = "/admin/login/"
    success_url = "/directories/genre/" 

class GenreList(generic.ListView):
    template_name="directories/genre_list.html"
    model = models.Genre
    login_url = "/admin/login/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
 
# CopyrightHolder
class CopyrightHolderCreate(LoginRequiredMixin, generic.CreateView):
    template_name="directories/copyrightholder_create.html"
    model = models.CopyrightHolder
    login_url = "/admin/login/"
    form_class = forms.CopyrightHolderModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CopyrightHolderUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="directories/copyrightholder_update.html"
    model = models.CopyrightHolder
    login_url = "/admin/login/"
    form_class = forms.CopyrightHolderModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CopyrightHolderDetail(LoginRequiredMixin, generic.DetailView):
    template_name="directories/copyrightholder_detail.html"
    login_url = "/admin/login/"
    model = models.CopyrightHolder

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class CopyrightHolderDelete(LoginRequiredMixin, generic.DeleteView):
    template_name="directories/copyrightholder_delete.html"
    model = models.CopyrightHolder
    login_url = "/admin/login/"
    success_url = "/directories/copyrightholder/" 

class CopyrightHolderList(generic.ListView):
    template_name="directories/copyrightholder_list.html"
    model = models.CopyrightHolder
    login_url = "/admin/login/"

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