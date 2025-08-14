from django.db import models
from organizations.models import OrganizationScopedModel


class Client(OrganizationScopedModel):
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=50, blank=True, default="")

	def __str__(self) -> str:
		return self.name
