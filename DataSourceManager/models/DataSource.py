from .DataSourceType import DataSourceType

from django.db import models

class DataSource(models.Model):
    id = models.AutoField(primary_key=True)
    connection_name = models.CharField(max_length=100,unique=True)
    type = models.ForeignKey(DataSourceType, on_delete=models.CASCADE, related_name='data_connections')
    data = models.JSONField()
    objects = models.Manager()


    def __str__(self):
        return f"{self.connection_name} ({self.type})"


