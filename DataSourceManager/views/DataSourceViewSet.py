from DataSourceManager.serializers.DataSourceSerializer import DataSourceSerializer
from DataSourceManager.models.DataSource import DataSource
from rest_framework import viewsets
class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer