from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("networks.urls"), name="networks"),
    path("users/", include("users.urls", namespace="users")),
]
