from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	list_display = ("id", "name", "client", "billable", "status", "organization")
	list_filter = ("organization", "billable", "status")
	search_fields = ("name", "code")
