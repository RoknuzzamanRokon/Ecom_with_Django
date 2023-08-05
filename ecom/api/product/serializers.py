from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    
    class meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'stock', 'image', 'category' )



