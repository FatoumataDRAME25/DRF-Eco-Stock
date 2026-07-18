from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import  Response

# Create your views here.
from .models import Warehouse, Product
from .serializers import WarehouseSerializer, ProductSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


    @action(detail = True, methods = ['get'])
    def audit(self, request, pk=None):
        warehouse = self.get_object()

        produit= Product.objects.filter(warehouse=warehouse)
        total_produit = produit.count()
        return Response({
            'entrepot': warehouse.nom,
            'capacite': warehouse.capacite,
            'total_produits': total_produit,
        })



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    @action(detail = True, methods =['post'])
    def move(self, request, pk = None):
        product = self.get_object()
        # Vérifier que le produit n'est pas périmé
        if product.etat == 'périmé':    # ou a la place de périmé on met Product.Etat.PERIME c'est plus optimisé
            return Response ({'error': "Produit périmé, transfert impossible."},
                              status=400
                            )
        # Transfere d'un produit vers un autre entrepot, 
        # ici l'instance du produit donne en premier parametre montre que ce n'est pas un crearion mais une modification, 
        # data=request.data conteint les nouvelles donnees envoyer par le body et 
        # partial=True montre c'est un PATCH pas un PUT 

        # raise_exception=True nous permet d'eviter les if/else pour la gestion des erreurs

        serializer = self.get_serializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
    

