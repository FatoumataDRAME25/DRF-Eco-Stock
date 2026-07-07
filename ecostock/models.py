from django.db import models

# Create your models here.


class Warehouse(models.Model):
    nom = models.CharField(max_length=128)
    localisation = models.CharField(max_length=64)
    capacite = models.PositiveIntegerField()


    def __str__(self):
        return self.nom
    
    class Meta:
        ordering = ['nom','-capacite']


class Product(models.Model):
    class Etat(models.TextChoices):
        
        DISPONIBLE = 'disponible', 'Disponible',
        RESERVE = 'réservé', 'Réservé',
        PERIME = 'périmé', 'Périmé'
        

    nom = models.CharField(max_length=64)
    quantite = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE, related_name='products')
    date_expiration = models.DateField()
    etat = models.CharField(max_length=20, choices=Etat.choices, default=Etat.DISPONIBLE)


    def __str__(self):
        return self.nom
    

    class Meta:
        ordering = ["nom", "date_expiration"]