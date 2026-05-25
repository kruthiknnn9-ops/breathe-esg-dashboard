from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    SOURCE_TYPES = [
        ('sap', 'SAP'),
        ('utility', 'Utility'),
        ('travel', 'Travel'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    file_name = models.CharField(max_length=255)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company.name} - {self.source_type}"


class EmissionRecord(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE
    )

    source = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    scope = models.CharField(max_length=20)

    category = models.CharField(max_length=100)

    activity_date = models.DateField()

    activity_value = models.FloatField()

    unit = models.CharField(max_length=50)

    normalized_value = models.FloatField(
        null=True,
        blank=True
    )

    normalized_unit = models.CharField(
        max_length=50,
        default='kg'
    )

    emission_factor = models.FloatField(default=0)

    co2e = models.FloatField(default=0)

    anomaly_flag = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    locked_for_audit = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.co2e}"


class AuditLog(models.Model):

    record = models.ForeignKey(
        EmissionRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=100)

    old_value = models.TextField(
        null=True,
        blank=True
    )

    new_value = models.TextField(
        null=True,
        blank=True
    )

    changed_by = models.CharField(max_length=255)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action