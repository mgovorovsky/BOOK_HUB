from rest_framework import serializers
from . import models

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = [
            'pk',
            'user',
            'order_bookname',
            'summ',
            'order_currency',
            'cover',
        ]
