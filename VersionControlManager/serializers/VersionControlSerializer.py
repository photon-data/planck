

from rest_framework import serializers
from VersionControlManager.models.VersionControl import VersionControl
from VersionControlManager.models.VersionControlType import VersionControlType
from .VersionControlTypeSerializer import VersionControlTypeSerializer

from rest_framework import serializers
from VersionControlManager.models import VersionControl, VersionControlType



class VersionControlSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='name', queryset=VersionControlType.objects.all())

    class Meta:
        model = VersionControl
        fields = ['id', 'connection_name', 'type', 'data']

    def validate(self, attrs):
        # Custom validation depending on the type of version control system
        vc_type = self.initial_data.get('type').lower()
        data = attrs.get('data')
        registered_types=list(VersionControlType.objects.values_list('name', flat=True))
        if vc_type in registered_types:
            required_fields = list(attrs.get('type').required_fields)
        else:
            raise serializers.ValidationError(f"Unsupported version control type: {vc_type}")

        # Check if all required fields are present in data
        missing_fields = [field for field in required_fields if field not in data]
        if missing_fields:
            raise serializers.ValidationError(f"Missing fields in data: {', '.join(missing_fields)}")

        return attrs
