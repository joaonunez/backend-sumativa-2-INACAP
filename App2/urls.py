from django.urls import path
from .views import agregar_producto, modificar_producto, eliminar_producto
from .views import agregar_categoria, modificar_categoria, eliminar_categoria

urlpatterns = [
    # Rutas para productos
    path('productos/', agregar_producto, name='agregar-producto'),
    path('productos/<int:pk>/', modificar_producto, name='modificar-producto'),
    path('productos/<int:pk>/delete/', eliminar_producto, name='eliminar-producto'),

    # Rutas para categorías
    path('categorias/', agregar_categoria, name='agregar-categoria'),
    path('categorias/<str:pk>/', modificar_categoria, name='modificar-categoria'),
    path('categorias/<str:pk>/delete/', eliminar_categoria, name='eliminar-categoria'),
]
