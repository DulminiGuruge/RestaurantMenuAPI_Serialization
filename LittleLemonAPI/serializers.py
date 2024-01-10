from rest_framework import serializers
from .models import MenuItem,Category
from decimal import Decimal


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','slug','title']


class MenuItemSerializer(serializers.ModelSerializer):
    #to change the name of the variable name
    stock = serializers.IntegerField(source='inventory')
    price_after_tax = serializers.SerializerMethodfield(method_name='calculate_tax')
    category = CategorySerializer(read_only = True)
    category_id =  serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        fields = ['id','title','price','stock','price_after_tax', 'category']

    def calculate_tax(self,product:MenuItem):
        return product.price * Decimal(1.1)    

