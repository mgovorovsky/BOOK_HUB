from django import template
import requests
from django.http import HttpResponse
from datetime import date
from orders import views as order_view
from django.urls import reverse_lazy
from django.utils.safestring import mark_safe

register = template.Library()

# tag
@register.simple_tag
def a_plus_b(a, b):
    return a + b

# filter 
@register.filter(name="multiplier")
def multiplier(value, arg):
    return " ".join([str(value) for _ in range(arg)])

@register.simple_tag
def currency_value():
    response = requests.get("https://api.nbrb.by/exrates/rates/431")
    data = response.json()
    usd_value = data.get("Cur_OfficialRate")
    # date_today = date.today()
    return (f"{usd_value} ") # ({date_today} UTC) 

# filter 
@register.filter( name="show_user_or_login")
def show_user_or_login(user_obj):
    result = ""
    if user_obj.is_authenticated:
        result =  user_obj.username
    else:
        result  = f'<a href="{reverse_lazy("accs:login")} ">Login</a>'
    return mark_safe(result)