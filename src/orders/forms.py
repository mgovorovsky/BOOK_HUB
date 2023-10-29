from django import forms
from django.core.exceptions import ValidationError 
from . import models

class OrderModelForm(forms.ModelForm):
    class Meta:
        model = models.Order
        fields = [
            'delivery_adress',
            'email',
            'telephone_number',
        ]
