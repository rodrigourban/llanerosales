from django.db import models
from inventory.models import Item


class OrderList(models.Model):
    created_at = models.DateField(auto_now_add=True)
    item = models.ForeignKey(
                            Item,
                            on_delete=models.CASCADE,
                            related_name="order_item"
                            )
    status = models.CharField(max_length=200, default="PENDIENTE")
    edited_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return ("Pedido {}".format(created_at))
