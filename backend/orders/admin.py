from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        '_id', 
        'user', 
        'status', 
        'total_price', 
        'is_paid', 
        'paid_at', 
        'is_delivered', 
        'delivered_at', 
        'created_at'
    )
    list_filter = ('status', 'is_paid', 'is_delivered', 'created_at')
    search_fields = ('_id', 'user__email', 'user__username')
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'paid_at', 'delivered_at')

    fieldsets = (
        ("Order Details", {
            'fields': ('user', 'payment_method', 'status')
        }),
        ("Prices", {
            'fields': ('tax_price', 'shipping_price', 'total_price')
        }),
        ("Status", {
            'fields': ('is_paid', 'paid_at', 'is_delivered', 'delivered_at')
        }),
        ("Timestamps", {
            'fields': ('created_at',)
        }),
    )


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # No extra empty forms
    fields = ('product', 'name', 'qty', 'price')
    readonly_fields = ('name',)
    autocomplete_fields = ('product',)  # If many products exist, enable autocomplete


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = (
        '_id', 
        'order', 
        'product', 
        'name', 
        'qty', 
        'price'
    )
    list_filter = ('order__status',)
    search_fields = ('product__name', 'order__user__email', 'order__user__username')
    ordering = ['order', 'product']
    autocomplete_fields = ('product', 'order')
    readonly_fields = ('name',)

# Add the inline for Order
OrderAdmin.inlines = [OrderItemInline]
