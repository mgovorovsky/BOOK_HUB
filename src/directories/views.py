from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from . import models, forms


# Create your views here.

# def take_a_look(request):
#     author_id = request.GET.get("an_author")
#     print(author_id)
#     # a_book_name = models.BookName.objects.last()
#     # the_author = a_book_name.author.name
#     an_author = models.Author.objects.get(pk=int(author_id))
#     authors_books = an_author.book_names.all()
#     books = ""
#     for book in authors_books:
#         books += f"book name: {book.name} <br>"
#     out  = f"""
# <h1> The last book is: </h1>
# books: <br>{books}
# <a href="/director/?an_autor={int(an_author.pk) - 1}">previous author</a>
# """
#     return HttpResponse (out)

def currency_detail(request, pk):
   # directories/currency/
    obj = models.Currency.objects.get(pk=pk)
    context = {"obj" : obj, "verb": "detail"}
    return render(
        request, 
        template_name="directories/currency_detail.html",
        context=context
    )

def currency_list(request):
    obj_list = models.Currency.objects.all()
    context = {"object_list" : obj_list, "verb": "list"}
    return render(
        request, 
        template_name="directories/currency_list.html",
        context=context
    )

# делаем модельную форму (CurrencyModelForm - которая берет данные из класса,
# а не из отдельной для каждого класса, еще раз описывающей поля)
def currency_create(request):
    template_name="directories/currency_create.html"
    if request.method == "GET":
        form = forms.CurrencyModelForm()
        context = {"verb": "create", "form": form}
    elif request.method == "POST":
        form = forms.CurrencyModelForm(request.POST)
        if form.is_valid():
            obj = form.save()
            print(form.instance.pk)
            return HttpResponseRedirect(f"/directories/currency/{obj.pk}")
        else: 
            context = {"verb": "create", "form": form}

    else:
        raise Exception ("Wrong method")
    return render(
            request, 
            template_name=template_name,
            context=context,
    )    

def currency_update(request, pk):
    if request.method == "GET":
        template_name="directories/currency_update.html",
        obj = models.Currency.objects.get(pk=pk)
        form = forms.CurrencyForm({
            "name": obj.name,
            "description": obj.description,
        })
        context = {"obj" : obj, "verb": "Update", "form": form}

    elif request.method == "POST":
        form = forms.CurrencyForm(request.POST)
        if form.is_valid():
            form.update_obj(pk)
            return HttpResponseRedirect(f"/directories/currency/{pk}")    

    else:
        raise Exception ("Wrong method")
    return render(
        request, 
        template_name=template_name,
        context=context
    )   

