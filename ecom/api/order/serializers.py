from rest_framework import serializers
from .models import Order



class OrderSerializer(serializers.HyperlinkedModelSerializers):
    class Meta:
        model = Order
        field = ('user')