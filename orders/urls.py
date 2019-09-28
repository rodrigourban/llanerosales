from django.urls.conf import path
from .views import (
    order_list,
    order_list_create
)
app_name = 'orders'

urlpatterns = [
    path('', order_list, name="index"),
    path('create', order_list_create, name="create-orderlist"),
    # path('delete/<int:pk>', name="delete-orderlist"),
    # path('delete/order/<int:pk>', name="delete-order"),
    # path('/<int:pk>', name="detail-order"),
    # path('topdf/<int:pk>', name="order-topdf"),
]
