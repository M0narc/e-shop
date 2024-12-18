from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    
    # Fields to display in the user list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'date_joined', 'date_update')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'date_joined')

    # Fields for searching users
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Fields for ordering the users
    ordering = ('-date_joined',)

    # Organize fields into sections in the detail/edit view
    fieldsets = (
        ('Personal Info', {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'avatar')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important Dates', {'fields': ('last_login', 'date_joined', 'date_update')}),
    )

    # Fields for the "Add User" form
    add_fieldsets = (
        ('Create User', {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'avatar', 'is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
    )

    readonly_fields = ('date_joined', 'date_update', 'last_login')