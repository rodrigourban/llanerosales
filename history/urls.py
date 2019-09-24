from django.urls.conf import path
from .views import sell_list, sell_item, cancel_sell

app_name = 'history'

urlpatterns = [
    path('', sell_list, name="index"),
    path('sell_item/<int:pk>', sell_item, name="sell-item"),
    path('cancel_sell/<int:pk>', cancel_sell, name="cancel-sell"),
]
