from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer


class IsOrgAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return getattr(request.user, "role", None) in {"owner", "admin"}


class TaskViewSet(viewsets.ModelViewSet):
	serializer_class = TaskSerializer
	permission_classes = [IsOrgAdminOrReadOnly]
	filterset_fields = ['project']
	search_fields = ['name', 'code']
	ordering_fields = ['name', 'id']

	def get_queryset(self):
		return Task.objects.filter(organization=self.request.user.organization)

	def perform_create(self, serializer):
		serializer.save(organization=self.request.user.organization)
