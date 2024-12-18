from django.contrib import admin
from .models import ShippingAddress


@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ('_id', 'order', 'address', 'city', 'country', 'shipping_price', 'created_at')
    list_filter = ('country', 'city')
    search_fields = ('address', 'city', 'postal_code', 'country')
    readonly_fields = ('_id', 'created_at')
