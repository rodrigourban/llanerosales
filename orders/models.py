from django.db import models
from inventory.models import Item


class OrderList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    edited_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return (f"Pedido {self.title}")


class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="order_item"
    )
    order_list = models.ForeignKey(
        OrderList,
        on_delete=models.CASCADE,
        related_name="order_list"
    )
    amount = models.IntegerField(default=0, blank=False)

    def __str__(self):
        return f"Order {self.item.name}"
