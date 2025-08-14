from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
	list_display = ("id", "username", "email", "organization", "role", "is_active")
	list_filter = ("organization", "role", "is_active")
	search_fields = ("username", "email")
