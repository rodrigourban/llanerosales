import os
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=200, unique=True)
    sku = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200)
    sell_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    buy_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    img = models.ImageField(
                            upload_to="imagenes",
                            default="imagenes/no-image.jpg")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def validate_fields(self):
        # Validate data and return bool
        pass

    def create(self, content):
        # Validate and create new
        item = self.__init__(content)
        item.save()

    def delete(self):
        # Soft delete article and stock related
        pass

    def update(self):
        # Valdate and Update one or more fields
        pass

    def detail(self):
        # Get and return element
        pass

    def get_list(self, filter=None, amount=None):
        # Return list of articles, should have pagination
        # and filter
        pass

    def sell(self):
        # Sells and article
        pass

    def get_fields(self):
        return [
            {'title': 'Imagen', 'filterable': True, 'type': 'image'},
            {'title': 'Nombre', 'filterable': True, 'type': 'string'},
            {'title': 'SKU', 'filterable': True, 'type': 'string'},
            {'title': 'Ubicacion', 'filterable': True, 'type': 'string'},
            {'title': 'Precio', 'filterable': True, 'type': 'float'},
            {'title': 'Costo', 'filterable': True, 'type': 'float'},
            {'title': 'Stock', 'filterable': True, 'type': 'integer'},
            ]


class Stock(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    amount = models.IntegerField(default=0)
    buy_price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return ("{} - {}".format(str(self.created_at), self.item.name))

    def create(self):
        # Create stock, attached to article
        pass

    def delete(self):
        # Soft delete
        pass

    def update(self):
        # update stock, for sales or when adding stock
        pass

    def get_list(self):
        # return a list of stocks
        pass
