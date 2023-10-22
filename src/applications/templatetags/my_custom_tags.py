from django import template

register = template.Library()

# # tag
# @register.simple_tag
# def a_plus_b(a, b):
#     return a + b

# # filter 
# @register.filter(name="multiplier")
# def multiplier(value, arg):
#     return " ".join([str(value) for _ in range(arg)])