from django.urls import path
from rest_framework.routers import DefaultRouter

from networks.apps import NetworksConfig
from networks.views import (
    ContactCreateAPIView,
    ContactDestroyAPIView,
    ContactDetailAPIView,
    ContactListAPIView,
    ContactUpdateAPIView,
    NetworkViewSet,
    ProductCreateAPIView,
    ProductDestroyAPIView,
    ProductDetailAPIView,
    ProductListAPIView,
    ProductUpdateAPIView,
)

app_name = NetworksConfig.name

router = DefaultRouter()
router.register(r"networks", NetworkViewSet, basename="networks")

urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="product-list"),
    path("products/create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),
    path("products/<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product-update"),
    path("products/<int:pk>/delete/", ProductDestroyAPIView.as_view(), name="product-delete"),
    path("contacts/", ContactListAPIView.as_view(), name="contact-list"),
    path("contacts/create/", ContactCreateAPIView.as_view(), name="contact-create"),
    path("contacts/<int:pk>/", ContactDetailAPIView.as_view(), name="contact-detail"),
    path("contacts/<int:pk>/update/", ContactUpdateAPIView.as_view(), name="contact-update"),
    path("contacts/<int:pk>/delete/", ContactDestroyAPIView.as_view(), name="contact-delete"),
] + router.urls
