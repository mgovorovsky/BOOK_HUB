from django import forms
from django.core.exceptions import ValidationError 
from . import models

# def my_validator(field):
#     if field == "xxx":
#        raise ValidationError("It can't be 'xxx'")

# class CurrencyForm(forms.Form):
#     name = forms.CharField(
#         max_length=3, 
#         required=True,
#         label="Currency name",
#         help_text="Please enter currency name",
#         validators=[my_validator]
#     )

#     description = forms.CharField(
#         required=False, 
#         widget=forms.Textarea()
#     )  

#     def save_obj(self):
#             name = self.cleaned_data.get("name")
#             description = self.cleaned_data.get("description")
#             obj = models.Currency.objects.create(
#                 name=name, 
#                 description=description
#             )
#             return obj


#     def update_obj(self, pk):
#         name = self.cleaned_data.get("name")
#         description = self.cleaned_data.get("description")
#         models.Currency.objects.filter(pk=pk).update(
#             name=name, 
#             description=description
#         )

class CurrencyModelForm(forms.ModelForm):
    class Meta:
        model = models.Currency
        fields = [
            'name',
            'description',

            ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = models.Author
        fields = [
            'name',
            'description',
            'copyright_holder'


            ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class SeriesModelForm(forms.ModelForm):
    class Meta:
        model = models.Series
        fields = [
            'name',
            'description',

            ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class BookNameModelForm(forms.ModelForm):
    class Meta:
        model = models.BookName
        fields = [
            'name',
            'author',
            'series',
            'genre',
            'description',

            ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class RatingModelForm(forms.ModelForm):
    class Meta:
        model = models.Rating
        fields = [
            'name',

            ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class AgeLimitModelForm(forms.ModelForm):
    class Meta:
        model = models.AgeLimit
        fields = [
            'name',

            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class BookTypeModelForm(forms.ModelForm):
    class Meta:
        model = models.BookType
        fields = [
            'name',
            'description',

            ]       
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class GenreModelForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = [
            'name',
            'description',

            ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class CopyrightHolderModelForm(forms.ModelForm):
    class Meta:
        model = models.CopyrightHolder
        fields = [
            'name',
            'description',

            ]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'