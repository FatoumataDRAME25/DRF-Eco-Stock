from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action

# Create your views here.
from .models import Warehouse, Product
from .serializers import WarehouseSerializer, ProductSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


   
        
