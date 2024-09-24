from django.db import models
import uuid
from django.core.exceptions import ValidationError
from .mixins.VersionControlValidationMixin import VersionControlValidationMixin

class VersionControlType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    required_fields = models.JSONField(default=dict)


    def __str__(self):
        return self.name

    objects = models.Manager()

    def delete(self, *args, **kwargs):
        if self.version_controls.exists():
            raise ValidationError(
                "Cannot delete this version control type because it has existing version control records.")
        super().delete(*args, **kwargs)
