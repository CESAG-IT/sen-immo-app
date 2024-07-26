

from django.contrib import admin
from django.urls import path, include

from core.views import dashboard

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("customers", include("customers.urls")),
    path("", dashboard, name="dashboard"),
]
