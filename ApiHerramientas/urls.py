from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'tipoProducto', TipoProductoViewSet)
router.register(r'producto', ProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]