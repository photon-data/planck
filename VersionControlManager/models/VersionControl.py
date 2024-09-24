from .VersionControlType import VersionControlType
from django.core.exceptions import ValidationError

from django.db import models
import uuid

class VersionControl(models.Model):
    id = models.AutoField(primary_key=True)
    connection_name = models.CharField(max_length=100,unique=True)
    type = models.ForeignKey(VersionControlType, on_delete=models.CASCADE, related_name='version_controls')
    data = models.JSONField()
    objects = models.Manager()


    def __str__(self):
        return f"{self.connection_name} ({self.type})"


