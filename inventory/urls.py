from django.urls.conf import path
from .views import article


urlpatterns = [
    path('', article),
]
