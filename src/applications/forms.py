from django import forms
from django.core.exceptions import ValidationError 
from . import models

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'user',
            'summ',
            'order_currency'
        ]