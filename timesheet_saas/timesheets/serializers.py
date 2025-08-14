from rest_framework import serializers
from .models import Timesheet, TimesheetEntry


class TimesheetEntrySerializer(serializers.ModelSerializer):
	class Meta:
		model = TimesheetEntry
		fields = ['id', 'timesheet', 'project', 'task', 'date', 'hours', 'notes', 'billable', 'organization', 'created_at', 'updated_at']
		read_only_fields = ['id', 'organization', 'created_at', 'updated_at']


class TimesheetSerializer(serializers.ModelSerializer):
	entries = TimesheetEntrySerializer(many=True, read_only=True)

	class Meta:
		model = Timesheet
		fields = ['id', 'user', 'week_start_date', 'status', 'entries', 'organization', 'created_at', 'updated_at']
		read_only_fields = ['id', 'organization', 'created_at', 'updated_at']