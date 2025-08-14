from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Client
from .serializers import ClientSerializer


class IsOrgAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return getattr(request.user, "role", None) in {"owner", "admin"}


class ClientViewSet(viewsets.ModelViewSet):
	serializer_class = ClientSerializer
	permission_classes = [IsOrgAdminOrReadOnly]

	def get_queryset(self):
		return Client.objects.filter(organization=self.request.user.organization)

	def perform_create(self, serializer):
		serializer.save(organization=self.request.user.organization)
