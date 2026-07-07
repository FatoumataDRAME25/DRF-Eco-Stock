from rest_framework import serializers
from .models import Warehouse, Product
from django.db.models import Sum


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id','nom', 'localisation', 'capacite']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','nom', 'quantite', 'warehouse', 'date_expiration', 'etat']

     # Fonction pour Vérifier que l'entrepôt de destination n'a pas atteint sa capacité
    def validate_warehouse(self, warehouse):
        autres_produits = Product.objects.filter(warehouse=warehouse)
        if self.instance:
            autres_produits = autres_produits.exclude(pk=self.instance.pk)
        
        total_actuel = autres_produits.aggregate(Sum('quantite'))['quantite__sum'] or 0
        quantite_a_ajouter = self.instance.quantite if self.instance else self.initial_data.get('quantite', 0)

        if total_actuel + quantite_a_ajouter > warehouse.capacite:
            raise serializers.ValidationError(
                f"L'entrepôt '{warehouse.nom}' n'a pas assez de place (capacité : {warehouse.capacite} kg) alors que {self.instance.nom} a {self.instance.quantite} kg."
            )

        return warehouse