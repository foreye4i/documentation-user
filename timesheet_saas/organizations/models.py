from django.db import models

# Create your models here.


class TimestampedModel(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


class Organization(TimestampedModel):
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True)
	plan = models.CharField(max_length=50, default="team")
	settings = models.JSONField(default=dict, blank=True)

	def __str__(self) -> str:
		return self.name


class OrganizationScopedModel(TimestampedModel):
	organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="%(class)ss")

	class Meta:
		abstract = True
