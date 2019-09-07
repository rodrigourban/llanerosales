from django.db import models


class Venta(models.Model):
    fecha = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    neto = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    bruto = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    costo = models.DecimalField(max_digits=15, decimal_places=2, default=0)
