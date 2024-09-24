from django.db import models
from django.core.exceptions import ValidationError

class DataSourceType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    required_fields = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    objects = models.Manager()

    def delete(self, *args, **kwargs):
        if self.data_connections.exists():
            raise ValidationError(
                "Cannot delete this version control type because it has existing version control records.")
        super().delete(*args, **kwargs)
