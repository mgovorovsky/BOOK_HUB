from django import forms
from django.core.exceptions import ValidationError 
from . import models

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'user',
            'order_bookname',
            'summ',
            'order_currency',
            'cover',
        ]
