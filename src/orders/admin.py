from django.contrib import admin
from . import models

class CartAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
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
    
admin.site.register(models.GoodInCart, GoodInCartAdmin)   
admin.site.register(models.Cart, CartAdmin)