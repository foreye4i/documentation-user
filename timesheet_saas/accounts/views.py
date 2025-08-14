from django.contrib.auth import get_user_model
from rest_framework import viewsets, permissions
from .serializers import UserSerializer

User = get_user_model()


class IsOrgAdminOrReadOnly(permissions.BasePermission):
	def has_permission(self, request, view):
		return request.user and request.user.is_authenticated

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		return getattr(request.user, "role", None) in {"owner", "admin"}


class UserViewSet(viewsets.ModelViewSet):
	serializer_class = UserSerializer
	permission_classes = [IsOrgAdminOrReadOnly]

	def get_queryset(self):
		user = self.request.user
		return User.objects.filter(organization=user.organization)

	def perform_create(self, serializer):
		serializer.save(organization=self.request.user.organization)
