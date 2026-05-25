# TRADEOFFS.md

# Deliberate Tradeoffs

## 1. No Real SAP API Integration

I did not implement:
- SAP OData
- BAPI
- IDoc ingestion

Reason:
These integrations require enterprise credentials and significantly increase infrastructure complexity.

The prototype focuses on realistic ingestion structure instead.

---

## 2. No OCR or PDF Parsing

Utility bills are often PDFs.

I intentionally avoided:
- OCR pipelines
- PDF extraction

Reason:
OCR accuracy and parsing logic would consume significant project time and distract from core normalization workflows.

---

## 3. No Advanced Workflow Permissions

The application does not include:
- RBAC
- auditor roles
- analyst approval queues

Reason:
The assignment prioritizes data modeling and ingestion realism over enterprise authentication systems.

---

# Future Improvements

- PostgreSQL production database
- async ingestion queues
- emission factor libraries
- analyst review workflows
- dashboard analytics
- real API integrations