from django.urls import path

from .views import index, create, update

urlpatterns = [
    path("", index, name="owners"),
    path("create", create, name="create-owner"),
    path("update/<int:id>", update, name="update-owner"),
]