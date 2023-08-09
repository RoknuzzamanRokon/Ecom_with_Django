from django.db import models
from api.user.models import CustomUser
from api.product.models import Product

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    
    product_name = models.CharField(max_length=250)
    product_description = models.CharField(max_length=250)
    product_price = models.CharField(max_length=50)
    product_stock = models.CharField(max_length=500)
    transaction_id = models.CharField(max_length=50)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    
    
    
    
    
    
    
    