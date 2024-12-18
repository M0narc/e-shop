from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'category',
        'price',
        'created_at'
    )

    list_filter = (
        'brand', 
        'category', 
        'created_at', 
        'rating'
        )
    
    search_fields = (
        'name',
        'user__first_name',
        'user__last_name',
        'category'
    )

    ordering = ('-created_at',)

    readonly_fields = ('created_at',)

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'brand', 'category', 'description', 'user')
        }),
        ('Stock & Pricing', {
            'fields': ('price', 'count_in_stock')
        }),
        ('Reviews & Ratings', {
            'fields': ('rating', 'num_reviews')
        }),
        ('Other Info', {
            'fields': ('created_at',)
        }),
    )

