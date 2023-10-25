from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView
from . import models
from directories import models as good_model 

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
        context={"cart": cart}

    )
    
class Cart(UpdateView):
    template_name = ""
    model = models.Cart


class DeleteGoodInCart(DeleteView):
    model = models.GoodInCart
    success_url = "/orders/cart"