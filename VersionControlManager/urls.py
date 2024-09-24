
from django.urls import path
from VersionControlManager.views.VersionControlViewSet import VersionControlViewSet
from VersionControlManager.views.VersionControlTypeViewSet import VersionControlTypeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'versioncontrol', VersionControlViewSet)
router.register(r'types/versioncontrol', VersionControlTypeViewSet)

urlpatterns = router.urls
