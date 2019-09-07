from django.db import models


class Pedido(models.Model):
    fecha = models.DateField(auto_now_add=True)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    estado = models.CharField(max_length=200, default="PENDIENTE")

    def __str__(self):
        return ("{} - {}".format(self.articulo.nombre, self.estado))
