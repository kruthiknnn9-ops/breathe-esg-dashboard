from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import (
    CompanyViewSet,
    DataSourceViewSet,
    EmissionRecordViewSet,
    AuditLogViewSet,
    upload_emissions_csv
)

router = DefaultRouter()

router.register(r'companies', CompanyViewSet)
router.register(r'sources', DataSourceViewSet)
router.register(r'emissions', EmissionRecordViewSet)
router.register(r'audit-logs', AuditLogViewSet)

urlpatterns = [
    path('', include(router.urls)),

    path('upload-csv/', upload_emissions_csv),
]