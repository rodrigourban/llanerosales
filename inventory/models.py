import os
from functools import reduce
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sku = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    sell_price = models.DecimalField(
                                    max_digits=15,
                                    decimal_places=2,
                                    default=0
                                    )
    buy_price = models.DecimalField(
                                    max_digits=15,
                                    decimal_places=2,
                                    default=0
                                    )
    img = models.ImageField(
                            upload_to="imagenes",
                            default="imagenes/no-image.png")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def validate_fields(self):
        # Validate data and return bool
        pass

    def sell(self):
        # Sells and article
        pass

    def get_fields():
        return [
            {'title': 'Imagen', 'filterable': False, 'type': 'image'},
            {'title': 'Nombre', 'filterable': True, 'type': 'string'},
            {'title': 'SKU', 'filterable': True, 'type': 'string'},
            {'title': 'Ubicacion', 'filterable': False, 'type': 'string'},
            {'title': 'Precio', 'filterable': True, 'type': 'float'},
            {'title': 'Costo', 'filterable': True, 'type': 'float'},
            {'title': 'Stock', 'filterable': False, 'type': 'integer'},
            {'title': 'Acciones', 'filterable': False, 'type': 'none'},
            ]

    def count_stock(self):
        return reduce(
                    lambda a, b: a + b,
                    [stock.amount for stock in Stock.objects.all().filter(item=self.pk, status=True)])

    def get_stock(self, pk):
        return [stock for stock in Stock.objects.all().filter(
                    item=pk,
                    status=True)]


class Stock(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=0)
    buy_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, blank=True)
    status = models.BooleanField(default=1)

    def __str__(self):
        return ("{} - {}".format(str(self.created_at), self.item.name))
