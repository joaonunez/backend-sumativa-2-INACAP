from django.shortcuts import render
from rest_framework import generics
from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer

# Vista para listar todos los productos ordenados por nombre
class ProductoListView(generics.ListAPIView):
    queryset = Producto.objects.all().order_by('nombre')
    serializer_class = ProductoSerializer

# Vista para obtener los detalles de un producto por ID
class ProductoDetailView(generics.RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

# Vista para listar todas las categorías
class CategoriaListView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

# Vista para obtener los detalles de una categoría por su código
class CategoriaDetailView(generics.RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    lookup_field = 'codigoCategoria'
