from django.contrib import admin
from . import models

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'customer',
        'good_quantity',
        'total_price',
        'created',
    ]

class GoodInCartAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'cart',
        'good',
        'quantity',
        'price',
        'total_price',
    ]
    

class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'cart_id',
        'delivery_adress',
        'email',
        'telephone_number',
    ]


admin.site.register(models.GoodInCart, GoodInCartAdmin)   
admin.site.register(models.Cart, CartAdmin)
admin.site.register(models.Order, OrderAdmin)