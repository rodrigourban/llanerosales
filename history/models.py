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
    stock = models.ForeignKey(on_delete=models.SET_NULL)
    status = models.BooleanField(default=True)

    def __str__(self):
        return "{} {}".format(created_at, stock.name)

    def get_earn(self):
        return {
            "bruto": self.sell_price * self.amount,
            "neto": (self.sell_price - self.stock.buy_price) * self.amount
        }
