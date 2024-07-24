from django.urls import path

from .views import login_user, logout_user, register_customer, register_owner


urlpatterns = [
    path("customer/register", register_customer, name="register_customer"),
    path("customer/owner", register_owner, name="register_owner"),
    path("login", login_user, name="login_user"),
    path("logout", logout_user, name="logout_user"),
]
