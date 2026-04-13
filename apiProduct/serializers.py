from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock']


class ReduceStockActionSerializer(serializers.Serializer):
    producto_id = serializers.IntegerField(required=True)
    cantidad = serializers.IntegerField(required=True, min_value=1)