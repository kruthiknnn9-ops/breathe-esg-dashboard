# SOURCES.md

# Research Summary

## 1. SAP Fuel & Procurement Data

Research:
- SAP export formats
- flat file exports
- OData services
- procurement spreadsheets

Findings:
SAP exports often contain:
- inconsistent column names
- plant codes
- mixed date formats
- inconsistent units

Prototype Handling:
The prototype uses CSV uploads representing simplified SAP export structures.

Ignored:
- multilingual SAP schemas
- ERP authentication
- live OData integration

---

## 2. Utility Electricity Data

Research:
- utility portal exports
- electricity billing structures

Findings:
Utility exports usually contain:
- billing periods
- meter readings
- kWh usage
- tariff metadata

Prototype Handling:
The prototype accepts CSV electricity exports.

Ignored:
- PDF bills
- OCR extraction
- utility APIs

---

## 3. Corporate Travel Data

Research:
- Concur
- Navan
- travel management systems

Findings:
Travel systems typically provide:
- booking IDs
- airport codes
- trip categories
- travel classes

Prototype Handling:
The prototype simplifies travel data into:
- flights
- hotels
- ground transport

Ignored:
- live API integrations
- airport distance calculations
- airline-specific factors

---

# Sample Data Design

Sample data includes:
- electricity consumption
- fuel usage
- business travel

Large activity values intentionally trigger anomaly detection to simulate analyst review workflows.