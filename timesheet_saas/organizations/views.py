from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Organization
from .serializers import OrganizationSerializer


class IsOwnerOrAdmin(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		return getattr(request.user, "role", None) in {"owner", "admin"}


class OrganizationViewSet(viewsets.ModelViewSet):
	serializer_class = OrganizationSerializer
	permission_classes = [IsOwnerOrAdmin]
	lookup_field = 'slug'

	def get_queryset(self):
		return Organization.objects.all()
