from django import forms
from django.core.exceptions import ValidationError 
from . import models

class SearchForm(forms.Form):
    query = forms.CharField()

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'cart',
            'delivery_adress',
            'email',
            'telephone_number',
        ]

class CartModelForm(forms.ModelForm):
    class Meta:
        model = models.Cart
        fields = [
            'customer',
            
        ]
