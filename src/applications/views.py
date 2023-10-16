from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from . import models, forms
from directories import models as directories_models
from django.contrib.auth import get_user_model
from django.views import generic

# User = get_user_model()

# def order_detail(request, pk):
#     obj = models.Order.objects.get(pk=pk)
#     context = {"obj" : obj, "verb": "detail"}
#     return render(
#         request, 
#         template_name="applications/order_detail.html",
#         context=context
#     )

# def order_list(request):
#     obj_list = models.Order.objects.all()
#     context = {"object_list" : obj_list, "verb": "list"}
#     return render(
#         request, 
#         template_name="applications/order_list.html",
#         context=context
#     )

# def order_create(request):
#     if request.method == "GET":
#         template_name="applications/order_create.html",
#         context = {"verb": "create"}
#     elif request.method == "POST":
#         name = request.POST.get("name")
#         description = request.POST.get("description")
#         print(name, description)
#         obj = models.Order.objects.create(name=name, description=description)
#         return HttpResponseRedirect(f"/applications/order/{obj.pk}")
#     else:
#         raise Exception ("Wrong method")
#     return render(
#         request, 
#         template_name=template_name,
#         context=context
#     )    

# def order_update(request, pk):
#     if request.method == "GET":
#         template_name="applications/order_update.html",
#         obj = models.Order.objects.get(pk=pk)
#         all_users = User.objects.all()
#         all_currencies = directories_models.Currency.objects.all()
#         context = {
#             "obj" : obj, 
#             "verb": "Update",
#             "all_users": all_users, 
#             "all_currencies": all_currencies,

#             }
#     elif request.method == "POST":
#         user_pk = request.POST.get("user")
#         summ = request.POST.get("summ")
#         order_currency_pk = request.POST.get("order_currency")
#         print(user_pk, summ, order_currency_pk)
#         obj = models.Order.objects.get(
#             user=User.objects.get(pk=int(user_pk)), 
#             summ=summ,
#             order_currency=directories_models.Currency.objects.get(pk=order_currency_pk)
#         )

#         return HttpResponseRedirect(f"/applications/order/{obj.pk}")    

#     else:
#         raise Exception ("Wrong method")
#     return render(
#         request, 
#         template_name=template_name,
#         context=context
#     )  

class OrderCreate(generic.CreateView):
    template_name="applications/order_create.html"
    model = models.Order
    form_class = forms.OrderModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context

class OrderUpdate(generic.UpdateView):
    template_name="applications/order_update.html"
    model = models.Order
    form_class = forms.OrderModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context

    # добавляем редирект урл для конкретной вью
    # def get_success_url(self):
    #     return f"/applications/order/{self.object.pk}/" 


class OrderDetail(generic.DetailView):
    template_name="applications/order_detail.html"
    model = models.Order

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    
class OrderDelete(generic.DeleteView):
    template_name="applications/order_delete.html"
    model = models.Order
    success_url = "/applications/order/" 

class OrderList(generic.ListView):
    template_name="applications/order_list.html"
    model = models.Order

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
 
    
class AboutUs(generic.TemplateView):
    template_name = "about_us.html"