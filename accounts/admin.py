from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # On garde la config UserAdmin de base
    fieldsets = UserAdmin.fieldsets + (("Infos supplémentaires", {"fields": ("bio",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("bio",)}),)
