from django.urls import path
from .views import ProductoListView, ProductoDetailView, CategoriaDetailView, CategoriaListView

urlpatterns = [
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/<int:pk>/', ProductoDetailView.as_view(), name='producto-detail'),
    # Rutas para categorías
    path('categorias/', CategoriaListView.as_view(), name='categoria-list'),
    path('categorias/<str:codigoCategoria>/', CategoriaDetailView.as_view(), name='categoria-detail'),
]
