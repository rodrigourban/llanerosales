from django.urls.conf import path
from .views import (
    admin_panel,
    create_user,
    delete_user,
)
app_name = 'admin-panel'

urlpatterns = [
    path('', admin_panel, name="index"),
    path('create/', create_user, name="create-user"),
    path('delete/<int:pk>', delete_user, name="delete-user")
]
