from VersionControlManager.serializers.VersionControlTypeSerializer import VersionControlTypeSerializer
from VersionControlManager.models.VersionControlType import VersionControlType
from rest_framework import viewsets
class VersionControlTypeViewSet(viewsets.ModelViewSet):
    queryset = VersionControlType.objects.all()
    serializer_class = VersionControlTypeSerializer