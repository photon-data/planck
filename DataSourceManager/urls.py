
from django.urls import path
from DataSourceManager.views.DataSourceTypeViewSet import DataSourceTypeViewSet
from DataSourceManager.views.DataSourceViewSet import DataSourceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'datasource', DataSourceViewSet)
router.register(r'types/datasource', DataSourceTypeViewSet)

urlpatterns = router.urls
