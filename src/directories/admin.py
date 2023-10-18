from django.contrib import admin
from . import models

admin.site.register(models.Author)
admin.site.register(models.Series)
admin.site.register(models.BookName)
admin.site.register(models.Rating)
admin.site.register(models.AgeLimit)
# admin.site.register(models.PaymentSystem)
# admin.site.register(models.BookType)
admin.site.register(models.Genre)
admin.site.register(models.CopyrightHolder)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'name',
        'description'
    ]
    
admin.site.register(models.Currency, CurrencyAdmin)