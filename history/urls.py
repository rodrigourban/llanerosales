from django.urls.conf import path
from .views import sell_item

app_name = 'history'

urlpatterns = [
    path(''),
    path('sell_item/<int:pk>', sell_item, name="sell-item"),
    path('cancel_sell/<int:pk>')
]
