from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
	class Role(models.TextChoices):
		OWNER = "owner", "Owner"
		ADMIN = "admin", "Admin"
		MANAGER = "manager", "Manager"
		MEMBER = "member", "Member"
		FINANCE = "finance", "Finance"

	organization = models.ForeignKey(
		"organizations.Organization",
		on_delete=models.CASCADE,
		null=True,
		blank=True,
		related_name="users",
	)
	role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)

	def __str__(self) -> str:
		return f"{self.username} ({self.organization_id})"
