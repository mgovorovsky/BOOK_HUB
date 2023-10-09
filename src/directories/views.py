from django.shortcuts import render
from django.http import HttpResponse
from random import randint
from . import models

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
   # references/currence/
    obj = models.Currency.objects.get(pk=pk)
    return HttpResponse (f"""
                        <h1>Currency Detail</h1>
                        currency name: {obj.name} </br>
                        currency description: {obj.description} </br>
                        """)

def currency_list(request):
    obj_list = models.Currency.objects.all()
    out = """<h1>Currencies: </h1>
            <td>id</td>
            <td>name</td>
            <td>descriptions</td>
            <td>actions</td>
            """

    for obj in obj_list:
        out += f"""
        <tr>
        <td>{obj.pk}</td><td>{obj.name}</td><td>{obj.description}</td><td></td>
        </tr>"""
    return HttpResponse(out)
