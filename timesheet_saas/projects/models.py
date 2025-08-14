from django.db import models
from organizations.models import OrganizationScopedModel


class Project(OrganizationScopedModel):
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=50, blank=True, default="")
	client = models.ForeignKey('clients.Client', on_delete=models.PROTECT, related_name='projects', null=True, blank=True)
	billable = models.BooleanField(default=True)
	status = models.CharField(max_length=20, default='active')

	def __str__(self) -> str:
		return self.name
