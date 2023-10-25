from django.db import models
from directories.models import BookName
from django.db.models import Sum
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        verbose_name="Customer", 
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    created = models.DateTimeField(
        verbose_name="Created date",
        auto_now=False, 
        auto_now_add=True,
    )

    def __str__(self):
        return f"cart {self.pk}" 
    
    @property
    def good_quantity(self):
        return self.goods.aggregate(total=Sum("quantity")).get("total", 0)
    
    @property
    def total_price(self):
        summ = 0
        for good_in_cart in self.goods.all():
            summ += good_in_cart.total_price
        return summ
    

class GoodInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        verbose_name="Cart",
        on_delete=models.CASCADE,
        related_name="goods",
    )

    good = models.ForeignKey(
        BookName,
        verbose_name="Good",
        on_delete=models.PROTECT,
        related_name="carts", 
    )

    quantity = models.PositiveIntegerField(
        verbose_name="Quantity",
        default=1,
    )

    def __str__(self):
        return f"Good: {self.good.name}, quantity: {self.quantity}"
    
    @property
    def price(self):
        return self.good.price
    
    @property
    def total_price(self):
        return self.quantity * self.good.price
    

# class Order(models.Model):
#     cart = models.ForeignKey(
#         Cart
#     )
#     delivery_adress = 
#     summ = 




