from django.db import models

# Create your models here.
class TipoProducto(models.Model):
    tipo_herramienta = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'TipoProducto'


    def __str__(self):
        return f"Tipo de producto: {self.tipo_herramienta}"

class Producto(models.Model):
    marca_producto = models.CharField(max_length=30, null=True)
    codigo_marca = models.CharField(max_length=30, null=True)
    nombre_producto = models.CharField(max_length=40, null=True)
    tipo_herramienta = models.ForeignKey(TipoProducto, null=True, on_delete=models.PROTECT)
    valor_producto = models.IntegerField(null=True)

    class Meta:
        db_table = 'Producto'


    def __str__(self):
        return f"Producto: {self.nombre_producto}"