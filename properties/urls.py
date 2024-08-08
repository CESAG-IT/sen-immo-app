from django.urls import path

from .views import index, create, update, delete

urlpatterns = [
    path("", index, name="properties"),
    path("create", create, name="create-property"),
    path("update/<int:id>", update, name="update-property"),
    path("delete/<int:id>", delete, name="delete-property")
]