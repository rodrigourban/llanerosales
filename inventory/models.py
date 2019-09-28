import os
from functools import reduce
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


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
    created_by = models.ForeignKey(
        User,
        null=True,
        related_name="item_user",
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    def validate_fields(self):
        # Validate data and return bool
        pass

    def get_fields():
        return [
            {'field': "img", 'title': 'Imagen', 'filterable': False, 'type': 'image'},
            {'field': "name", 'title': 'Nombre', 'filterable': True, 'type': 'string'},
            {'field': "sku", 'title': 'SKU', 'filterable': True, 'type': 'string'},
            {'field': "location", 'title': 'Ubicacion', 'filterable': False, 'type': 'string'},
            {'field': "sell_price", 'title': 'Precio', 'filterable': True, 'type': 'float'},
            {'field': "buy_price", 'title': 'Costo', 'filterable': True, 'type': 'float'},
            {'field': "created_at", 'title': 'Fecha', 'filterable': True, 'type': 'string'},
            {'field': "stock", 'title': 'Stock', 'filterable': False, 'type': 'integer'},
            {'field': "actions", 'title': 'Acciones', 'filterable': False, 'type': 'none'},
            ]

    def count_stock(self):
        if Stock.objects.filter(item=self.pk, status=True).count() > 0:
            return reduce(
                    lambda a, b: a + b,
                    [stock.amount for stock in Stock.objects.filter(item=self.pk, status=True)])
        else:
            return 0

    def get_stock(self, pk):
        return [stock for stock in Stock.objects.all().filter(
                    item=pk,
                    status=True)]


class Stock(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=0)
    buy_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    item = models.ForeignKey(
                            Item,
                            on_delete=models.CASCADE,
                            null=True,
                            related_name="stock_item")
    status = models.BooleanField(default=1)
    created_by = models.ForeignKey(
        User,
        null=True,
        related_name="stock_user",
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return ("{} - {}".format(str(self.created_at), self.item.name))

    def sell(self, amount, sell_price, user):
        remaining = 0
        if amount >= self.amount:
            remaining = amount - self.amount
            sell = Sell.objects.create(
                created_by=user,
                stock=self,
                sell_price=sell_price,
                amount=self.amount
            ).save()
            self.amount = 0
            self.status = False
        else:
            sell = Sell.objects.create(
                created_by=user,
                stock=self,
                sell_price=sell_price,
                amount=amount
            ).save()
            self.amount -= amount
        self.save()
        return remaining
