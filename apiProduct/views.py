from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db import transaction
from drf_spectacular.utils import extend_schema # <- Importante para Swagger
from .models import Product
from .serializers import ProductSerializer, ReduceStockActionSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    
    @extend_schema(request=ReduceStockActionSerializer(many=True))
    @action(detail=False, methods=['post'], url_path='reduce-stock')
    def reduce_stock(self, request):
        
        serializer = ReduceStockActionSerializer(data=request.data, many=True)
        
        
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        valid_items = serializer.validated_data
        
        with transaction.atomic():
            for item in valid_items:
                try:
                    prod = Product.objects.select_for_update().get(id=item['id'])
                    if prod.stock < item['quantity']:
                        return Response({"error": f"Falta stock para el producto {prod.id}"}, status=status.HTTP_400_BAD_REQUEST)
                    
                    prod.stock -= item['quantity']
                    prod.save()
                except Product.DoesNotExist:
                     return Response({"error": f"El producto {item['id']} no existe"}, status=status.HTTP_404_NOT_FOUND)
                     
        return Response({"message": "Stock reducido con validación estricta"}, status=status.HTTP_200_OK)