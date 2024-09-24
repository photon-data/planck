

from rest_framework import serializers
from DataSourceManager.models.DataSourceType import DataSourceType

class DataSourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSourceType
        fields = ['id', 'name','required_fields']