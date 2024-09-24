from VersionControlManager.serializers.VersionControlSerializer import VersionControlSerializer
from VersionControlManager.models.VersionControl import VersionControl
from rest_framework import viewsets

class VersionControlViewSet(viewsets.ModelViewSet):
    queryset = VersionControl.objects.all()
    serializer_class = VersionControlSerializer