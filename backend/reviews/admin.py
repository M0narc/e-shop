from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        '_id', 
        'product', 
        'user', 
        'name', 
        'rating', 
        'comment_short', 
    )
    list_filter = ('rating', 'product', 'user')
    search_fields = ('product__name', 'user__email', 'user__username', 'name', 'comment')
    ordering = ['-rating', 'product']
    readonly_fields = ('_id',)

    def comment_short(self, obj):
        """Show a truncated version of the comment."""
        return obj.comment[:50] + "..." if obj.comment and len(obj.comment) > 50 else obj.comment

    comment_short.short_description = "Comment Preview"
