from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "code", "organization")
	list_filter = ("organization",)
	search_fields = ("name", "code")
