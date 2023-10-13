from django import forms

class CurrencyForm(forms.Form):
    name = forms.CharField(
        max_length=3, 
        required=True,
        label="Currency name",
        help_text="Please enter currency name"
    )
    decsription = forms.CharField(
        required=False, 
        widget=forms.Textarea()
    )  
