# import serializer from rest_framework
from rest_framework import serializers
 
from .models import Category
# create a serializer

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        field = ('name', 'description')
        
        
        
        
        
        
        
        