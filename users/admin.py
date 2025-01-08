from django.contrib import admin

from users.models import CustomUserModel


@admin.register(CustomUserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_active', 'date_joined']
    search_fields = ['username']
    list_filter = ['date_joined']
