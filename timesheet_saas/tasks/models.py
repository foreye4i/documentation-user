from django.db import models
from organizations.models import OrganizationScopedModel


class Task(OrganizationScopedModel):
	name = models.CharField(max_length=255)
	code = models.CharField(max_length=50, blank=True, default="")
	project = models.ForeignKey('projects.Project', on_delete=models.CASCADE, related_name='tasks')

	def __str__(self) -> str:
		return self.name
