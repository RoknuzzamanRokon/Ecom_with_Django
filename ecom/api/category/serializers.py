# import serializer from rest_framework
from rest_framework import serializers
 
from .models import Category
# create a serializer

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'description')
        
        
        
        
        
        
        
        