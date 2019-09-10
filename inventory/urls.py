from django.urls.conf import path
from .views import (
    article,
    create_item,
    delete_item,
    sell_item,
    list_stock,
    create_stock
)

app_name = 'inventory'

urlpatterns = [
    path('', article, name="index"),
    path('create_item', create_item, name="create-item"),
    path('delete_item/<int:pk>', delete_item, name="delete-item"),
    path('sell_item/<int:pk>', sell_item, name="sell-item"),
    path('list_stock/<int:pk>', list_stock, name="list-stock"),
    path('create_stock/<int:pk>', create_stock, name="create-stock"),
]
