from DataSourceManager.serializers.DataSourceTypeSerializer import DataSourceTypeSerializer
from DataSourceManager.models.DataSourceType import DataSourceType
from rest_framework import viewsets
class DataSourceTypeViewSet(viewsets.ModelViewSet):
    queryset = DataSourceType.objects.all()
    serializer_class = DataSourceTypeSerializer