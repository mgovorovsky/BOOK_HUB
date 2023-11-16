from rest_framework import viewsets
from . import serializers
from . import models

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()
    # 5 views -> 5 paths