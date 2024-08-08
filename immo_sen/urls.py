

from django.contrib import admin
from django.urls import path, include

from core.views import dashboard

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("accounts.urls")),
    path("customers/", include("customers.urls")),
    path("owners/", include("owners.urls")),
    path("properties/", include("properties.urls")),
    path("", dashboard, name="dashboard"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)