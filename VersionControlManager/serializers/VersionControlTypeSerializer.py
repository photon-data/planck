

from rest_framework import serializers
from VersionControlManager.models.VersionControlType import VersionControlType

class VersionControlTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionControlType
        fields = ['id', 'name']