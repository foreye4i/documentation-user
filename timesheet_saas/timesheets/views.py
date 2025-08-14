from django.shortcuts import render
from rest_framework import viewsets, permissions, decorators, response, status
from .models import Timesheet, TimesheetEntry
from .serializers import TimesheetSerializer, TimesheetEntrySerializer


class IsOrgMember(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		return obj.organization_id == request.user.organization_id


class TimesheetViewSet(viewsets.ModelViewSet):
	serializer_class = TimesheetSerializer
	permission_classes = [IsOrgMember]
	filterset_fields = ['status', 'user', 'week_start_date']
	ordering_fields = ['week_start_date', 'id']

	def get_queryset(self):
		return Timesheet.objects.filter(organization=self.request.user.organization)

	def perform_create(self, serializer):
		serializer.save(organization=self.request.user.organization)

	@decorators.action(detail=True, methods=['post'])
	def submit(self, request, pk=None):
		timesheet = self.get_object()
		timesheet.status = Timesheet.Status.SUBMITTED
		timesheet.save(update_fields=['status'])
		return response.Response({'status': timesheet.status})

	@decorators.action(detail=True, methods=['post'])
	def approve(self, request, pk=None):
		if getattr(request.user, 'role', None) not in {"owner", "admin", "manager", "finance"}:
			return response.Response({'detail': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
		timesheet = self.get_object()
		timesheet.status = Timesheet.Status.APPROVED
		timesheet.save(update_fields=['status'])
		return response.Response({'status': timesheet.status})

	@decorators.action(detail=True, methods=['post'])
	def reject(self, request, pk=None):
		if getattr(request.user, 'role', None) not in {"owner", "admin", "manager", "finance"}:
			return response.Response({'detail': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
		timesheet = self.get_object()
		timesheet.status = Timesheet.Status.REJECTED
		timesheet.save(update_fields=['status'])
		return response.Response({'status': timesheet.status})


class TimesheetEntryViewSet(viewsets.ModelViewSet):
	serializer_class = TimesheetEntrySerializer
	permission_classes = [IsOrgMember]
	filterset_fields = ['project', 'task', 'date', 'billable']
	ordering_fields = ['date', 'id']

	def get_queryset(self):
		return TimesheetEntry.objects.filter(organization=self.request.user.organization)

	def perform_create(self, serializer):
		serializer.save(organization=self.request.user.organization)
