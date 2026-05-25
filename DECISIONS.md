# DECISIONS.md

# Key Decisions

## 1. CSV Upload Instead of Direct SAP Integration

I chose CSV upload ingestion for the prototype because:
- enterprise SAP integrations are complex
- OData/BAPI integrations require credentials and infrastructure
- CSV exports are common operational workflows

The prototype focuses on ingestion normalization rather than enterprise connectivity.

---

## 2. Utility Data as CSV Export

Utility data was modeled as CSV exports from utility portals.

Reason:
- many facilities teams manually export billing data
- CSV is easier to validate during ingestion
- PDF parsing/OCR introduces unnecessary complexity for a prototype

---

## 3. Travel Data Simplification

Travel emissions were simplified into:
- flights
- hotels
- ground transport

Real travel systems often provide:
- airport codes
- booking IDs
- distance estimates

The prototype focuses on normalized ingestion structure rather than complete travel emissions modeling.

---

## 4. Django + React Architecture

I chose:
- Django REST Framework for backend APIs
- React for analyst dashboard UI

Reason:
- rapid prototyping
- strong ecosystem
- easy API integration
- scalable architecture

---

## 5. SQLite for Development

SQLite was used during development for simplicity and portability.

Production deployment can migrate to PostgreSQL without major schema changes.

---

# Questions I Would Ask PM

- What ingestion volume is expected?
- Are uploads batch-based or continuous?
- Should auditors have separate permissions?
- Are emission factors region-specific?
- Is historical versioning required?