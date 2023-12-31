from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView
from . import models, forms
from directories import models as good_model 
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def update_cart(request):
    cart = None
    # cart = models.Cart.objects.create(
    # customer = request.user
    cart_id = request.session.get("cart_id")
    quantity = request.GET.get("quantity")
    good_pk = request.GET.get("good")
    action = request.GET.get("action")
    if quantity and good_pk:
        user = request.user
        if request.user.is_anonymous:
            user = None
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_id, 
            defaults={
                "customer": user
            }
        )   

        if created:
            request.session["cart_id"] = cart.pk

        good = good_model.BookName.objects.get(pk=int(good_pk))
        good_in_cart, created = models.GoodInCart.objects.get_or_create( 
            cart=cart,
            good=good,
            defaults={
                "quantity": int(quantity),

            }
        )

        if not created:
            if action == "edit":
                good_in_cart.quantity = int(quantity)
            else:
                good_in_cart.quantity = good_in_cart.quantity + int(quantity)
                good_in_cart.save()
            if good_in_cart.quantity <= 0:
                good_in_cart.delete()
            else:
                good_in_cart.save()

    else:
        cart = models.Cart.objects.filter(pk=cart_id)
        if cart:
            cart = cart[0]
    return cart



def cart(request):
    cart = update_cart(request)
    return render(
        request=request,
        template_name="orders/cart.html",
        context={"cart": cart},

    )

# def cart_upd(self, pk, *args, **kwargs):
#     pk = pk
#     cart = update_cart(pk) 
#     return render(
#         template_name="orders/cart.html",
#         context={"cart": cart},

#     )
    
class Cart(LoginRequiredMixin, generic.UpdateView):
    template_name="orders/cart.html"
    login_url = "/admin/login/"
    model = models.Cart
    form_class = forms.OrderModelForm
    success_url = "/orders/order_list/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "update"
        return context
    
class CartUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="orders/cart_update.html"
    login_url = "/admin/login/"
    model = models.Cart
    form_class = forms.OrderModelForm
    success_url = "/orders/order_list/"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "update"
        return context
    

class DeleteGoodInCart(DeleteView):
    model = models.GoodInCart
    success_url = "/orders/cart"


# def ordered_cart(request):
#     cart = update_cart(request)
#     return render(
#         request=request,
#         template_name="orders/order.html",
#         context={"cart": cart},

#     )

def order_success(request):
    cart_id = request.session.get("cart_id")
    if cart_id == None:
        return render(
            request=request,
            template_name="orders/order_empty.html",
        )
    
    else:
        del request.session["cart_id"]
        return render(
            request=request,
            template_name="orders/order_success.html",
        
        )
    
class OrderCreate(generic.CreateView):
    template_name="orders/order_data.html"
    model = models.Order
    form_class = forms.OrderModelForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        cart_id = self.request.session.get("cart_id")
        context["cart_id"] = cart_id
        cart = models.Cart.objects.get(
            pk=cart_id
        )   
        context["cart"] = cart
        return context
    
    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        cart_id = self.request.session.get("cart_id")
        cart = models.Cart.objects.get(
            pk=cart_id
        )   
        initial['cart'] = cart
        return initial
    

class OrderList(LoginRequiredMixin, generic.ListView):
    template_name="orders/portal_order_list.html"
    login_url = "/admin/login/"
    model = models.Order
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "list"
        return context
    
class OrderDelete(LoginRequiredMixin, generic.DeleteView):
    template_name="orders/portal_order_delete.html"
    model = models.Order
    login_url = "/admin/login/"
    success_url = "/orders/order_list/" 

class OrderUpdate(LoginRequiredMixin, generic.UpdateView):
    template_name="orders/portal_order_update.html"
    model = models.Order
    login_url = "/admin/login/"
    form_class = forms.OrderModelForm
    success_url = "/orders/order_list/" 

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["verb"] = "detail"
        return context
    

def portal_view(request):
    return render(
        request=request,
        template_name = "orders/portal_main.html",
        )



# from .forms import EmailPostForm, CommentForm, SearchForm
# from haystack.query import SearchQuerySet

# def post_search(request):
#     form = SearchForm()
    # if 'query' in request.GET:
    #     form = SearchForm(request.GET)
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         results = SearchQuerySet().models(Post).filter(content=cd['query']).load_all()
    #         # count total results
    #         total_results = results.count()
    # return render(request,
    #               'blog/post/search.html',
    #               {'form': form,
    #                'cd': cd,
    #                'results': results,
    #                'total_results': total_results})