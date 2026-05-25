# breathe-esg-dashboard
Full-stack ESG emissions review platform built with React, Django REST Framework, CSV ingestion, CO2e calculations, and anomaly detection.

# Breathe ESG Dashboard

A full-stack ESG emissions review platform built using React and Django REST Framework.

## Features

- CSV Upload
- ESG Emissions Tracking
- CO2e Calculation
- Anomaly Detection
- REST APIs
- Django Admin Dashboard
- React Frontend

## Tech Stack

Frontend:
- React
- Tailwind CSS
- Axios

Backend:
- Django
- Django REST Framework
- SQLite

## Setup

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate

pip install django djangorestframework pandas

python manage.py migrate
python manage.py runserver
```

## Sample CSV Format

```csv
scope,category,activity_date,activity_value,unit
Scope 2,Electricity,2025-01-10,500,kWh
```
