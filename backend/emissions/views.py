import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import viewsets

from .models import (
    Company,
    DataSource,
    EmissionRecord,
    AuditLog
)

from .serializers import (
    CompanySerializer,
    DataSourceSerializer,
    EmissionRecordSerializer,
    AuditLogSerializer
)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class DataSourceViewSet(viewsets.ModelViewSet):
    queryset = DataSource.objects.all()
    serializer_class = DataSourceSerializer


class EmissionRecordViewSet(viewsets.ModelViewSet):
    queryset = EmissionRecord.objects.all()
    serializer_class = EmissionRecordSerializer


class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer

@api_view(['POST'])
def upload_emissions_csv(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            'error': 'No file uploaded'
        }, status=400)

    df = pd.read_csv(file)

    records_created = 0

    company, _ = Company.objects.get_or_create(
        name='Demo Company'
    )

    source = DataSource.objects.create(
        company=company,
        source_type='utility',
        file_name=file.name
    )

    for _, row in df.iterrows():

        activity_value = float(row.get('activity_value', 0))

        emission_factor = 0.5

        co2e = activity_value * emission_factor

        anomaly = activity_value > 10000

        EmissionRecord.objects.create(
            company=company,
            source=source,
            scope=row.get('scope', 'Scope 2'),
            category=row.get('category', 'Electricity'),
            activity_date=row.get('activity_date'),
            activity_value=activity_value,
            unit=row.get('unit', 'kWh'),
            normalized_value=activity_value,
            normalized_unit='kWh',
            emission_factor=emission_factor,
            co2e=co2e,
            anomaly_flag=anomaly,
        )

        records_created += 1

    return Response({
        'message': 'CSV uploaded successfully',
        'records_created': records_created
    })