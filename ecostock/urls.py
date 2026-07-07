from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WarehouseViewSet, ProductViewSet

router = DefaultRouter()
router.register('entrepot', WarehouseViewSet)
router.register('produits', ProductViewSet)

urlpatterns = [
    path('', include(router.urls))
]
