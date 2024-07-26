from django.urls import path

from .views import index, create, update

urlpatterns = [
    path("", index, name="customers"),
    path("create", create, name="create-customer"),
    path("update/<int:id>", update, name="update-customer"),
]
