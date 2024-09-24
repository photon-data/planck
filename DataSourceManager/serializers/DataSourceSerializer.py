
from rest_framework import serializers
from DataSourceManager.models import DataSourceType, DataSource



class DataSourceSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', queryset=DataSourceType.objects.all())

    class Meta:
        model = DataSource
        fields = ['id', 'connection_name', 'type', 'data']

    def validate(self, attrs):
        # Custom validation depending on the type of data source
        ds_type = self.initial_data.get('type').lower()
        data = attrs.get('data')
        registered_types=list(DataSourceType.objects.values_list('name', flat=True))
        if ds_type in registered_types:
            required_fields = list(attrs.get('type').required_fields)
        else:
            raise serializers.ValidationError(f"Unsupported version control type: {ds_type}")

        # Check if all required fields are present in data
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise serializers.ValidationError(f"Missing fields in data: {', '.join(missing_fields)}")

        return attrs
