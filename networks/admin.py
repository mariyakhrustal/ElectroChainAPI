from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from networks.models import Contact, Network, Product


@admin.register(Network)
class NetworkAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "supplier",
        "debt",
        "level",
        "supplier_link",
        "created_at",
    )
    list_filter = (
        "contact__city",
        "level",
    )
    search_fields = (
        "name",
        "supplier",
    )
    readonly_fields = (
        "level",
        "created_at",
        "supplier_link",
    )
    actions = ["clear_debt"]

    @admin.display(description="Ссылка на поставщика")
    def supplier_link(self, obj):
        if obj.supplier:
            url = reverse("admin:networks_network_change", args=(obj.supplier.id,))
            return format_html('<a href="{}">{}</a>', url, obj.supplier.name)
        return "-"

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        queryset.update(debt=0)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "country",
        "city",
        "street",
        "house_number",
        "network",
    )
    list_filter = (
        "city",
        "country",
    )
    search_fields = (
        "email",
        "country",
        "city",
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "model",
        "release_date",
        "network",
    )
    list_filter = (
        "name",
        "model",
        "network",
    )
    search_fields = (
        "network",
        "name",
        "model",
    )
