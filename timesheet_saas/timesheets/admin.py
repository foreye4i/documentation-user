from django.contrib import admin
from .models import Timesheet, TimesheetEntry

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "week_start_date", "status", "organization")
	list_filter = ("organization", "status")
	search_fields = ("user__username",)

@admin.register(TimesheetEntry)
class TimesheetEntryAdmin(admin.ModelAdmin):
	list_display = ("id", "timesheet", "date", "hours", "project", "task", "billable", "organization")
	list_filter = ("organization", "billable")
	search_fields = ("notes",)
