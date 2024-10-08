from django.db import models

class Categoria(models.Model):
    codigoCategoria = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre


class Producto(models.Model):
    codigoProducto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.IntegerField()
    codigoBarra = models.CharField(max_length=13)
    codigoCategoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
