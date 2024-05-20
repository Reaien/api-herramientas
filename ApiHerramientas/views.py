from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import *
from .serializers import *
# Create your views here.
class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer