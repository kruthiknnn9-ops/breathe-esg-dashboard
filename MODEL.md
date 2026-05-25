# MODEL.md

## Overview

The application is designed as a multi-tenant ESG emissions ingestion and review platform.

The system ingests emissions and activity data from multiple enterprise sources:
- SAP exports
- Utility electricity exports
- Corporate travel data

The backend normalizes source data into a common emissions schema and allows analysts to review and approve records before audit lock.

---

# Core Models

## Company

Represents a tenant organization using the platform.

Fields:
- name
- created_at

Purpose:
Supports multi-tenancy by associating all records with a specific company.

---

## DataSource

Represents the origin of imported ESG data.

Fields:
- company
- source_type
- file_name
- uploaded_at

Supported source types:
- SAP
- Utility
- Travel

Purpose:
Tracks source-of-truth lineage for auditability.

---

## EmissionRecord

Central normalized ESG emissions model.

Fields:
- company
- source
- scope
- category
- activity_date
- activity_value
- unit
- normalized_value
- normalized_unit
- emission_factor
- co2e
- anomaly_flag
- status
- locked_for_audit
- created_at

Purpose:
Stores normalized emissions data across all ingestion sources.

---

# Scope Categorization

The platform supports:
- Scope 1
- Scope 2
- Scope 3

Examples:
- Fuel combustion → Scope 1
- Purchased electricity → Scope 2
- Business travel → Scope 3

---

# Unit Normalization

Different source systems provide inconsistent units.

Examples:
- kWh
- Liters
- km

The platform stores:
- original value
- normalized value
- normalized unit

This allows downstream calculations to use consistent units.

---

# Auditability

Audit support is implemented using:
- source tracking
- upload timestamps
- approval status
- audit lock fields

Once records are approved, they can be locked for audit review.

---

# AuditLog

Tracks changes to emissions records.

Fields:
- record
- action
- old_value
- new_value
- changed_by
- timestamp

Purpose:
Provides traceability for compliance and external audit workflows.