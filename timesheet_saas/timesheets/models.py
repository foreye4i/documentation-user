from django.db import models
from organizations.models import OrganizationScopedModel


class Timesheet(OrganizationScopedModel):
	class Status(models.TextChoices):
		DRAFT = "draft", "Draft"
		SUBMITTED = "submitted", "Submitted"
		APPROVED = "approved", "Approved"
		REJECTED = "rejected", "Rejected"
		LOCKED = "locked", "Locked"

	user = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='timesheets')
	week_start_date = models.DateField()
	status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

	class Meta:
		unique_together = ("organization", "user", "week_start_date")

	def __str__(self) -> str:
		return f"TS {self.user_id} {self.week_start_date} ({self.status})"


class TimesheetEntry(OrganizationScopedModel):
	timesheet = models.ForeignKey(Timesheet, on_delete=models.CASCADE, related_name='entries')
	project = models.ForeignKey('projects.Project', on_delete=models.PROTECT)
	task = models.ForeignKey('tasks.Task', on_delete=models.PROTECT)
	date = models.DateField()
	hours = models.DecimalField(max_digits=5, decimal_places=2)
	notes = models.CharField(max_length=500, blank=True, default="")
	billable = models.BooleanField(default=True)

	class Meta:
		indexes = [
			models.Index(fields=["organization", "date"]),
		]

	def __str__(self) -> str:
		return f"{self.date} {self.hours}h"
