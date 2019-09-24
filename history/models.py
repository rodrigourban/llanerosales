from django.db import models
from inventory.models import Stock


class Sell(models.Model):
    created_at = models.DateField(auto_now_add=True)
    amount = models.IntegerField(default=0)
    sell_price = models.DecimalField(
                                    max_digits=10,
                                    decimal_places=2,
                                    default=0
                                    )
    stock = models.ForeignKey(
                            Stock,
                            null=True,
                            on_delete=models.SET_NULL,
                            related_name="sell_stock",
                            )
    status = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(created_at, stock.name)

    def get_bruto(self):
        return self.sell_price * self.amount

    def get_neto(self):
        return (self.sell_price - self.stock.buy_price) * self.amount

    def cancel_sell(self):
        self.status = False
        self.save()
        self.stock.amount += self.amount
        self.stock.status = True
        self.stock.save()

    def get_headers():
        return [
            {
                'field': 'created_at',
                'title': 'Fecha de creacion',
                'filterable': True,
                'type': 'Date'
            },
            {
                'field': 'amount',
                'title': 'Cantidad',
                'filterable': True,
                'type': 'int'
            },
            {
                'field': 'item_name',
                'title': 'Articulo',
                'filterable': True,
                'type': 'string'
            },
            {
                'field': 'buy_price',
                'title': 'Costo',
                'filterable': True,
                'type': 'Date'
            },
            {
                'field': 'sell_price',
                'title': 'Venta',
                'filterable': True,
                'type': 'float'
            },
            {
                'field': 'bruto',
                'title': 'Bruto',
                'filterable': True,
                'type': 'float'
            },
            {
                'field': 'neto',
                'title': 'Neto',
                'filterable': True,
                'type': 'float'
            },
        ]
