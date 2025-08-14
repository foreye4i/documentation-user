from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "project", "organization")
	list_filter = ("organization",)
	search_fields = ("name", "code")
