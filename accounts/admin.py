from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Rôle', {'fields': ('role', 'entreprise')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Rôle', {'fields': ('role', 'entreprise')}),
    )
    list_display = ('username', 'email', 'role', 'entreprise', 'is_staff')
    list_filter = ('role',)