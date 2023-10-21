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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
