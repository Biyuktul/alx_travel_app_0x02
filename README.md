# alx_travel_app_0x02

## Milestone 3: Creating Views and API Endpoints

This milestone delivers API endpoints for managing listings and bookings, enabling full CRUD operations and interactive API documentation for the Django-based travel platform.

---

### Project Overview

This repository introduces REST API endpoints for the core models using Django REST Framework viewsets, and organizes URLs to follow standard RESTful practices. All endpoints are automatically documented via Swagger.

---

### Key Features

- ViewSets for `Listing` and `Booking` in `listings/views.py` (using `ModelViewSet` for CRUD operations)
- RESTful API endpoints under `/api/` using DRF routers, configured in `listings/urls.py`
- Automated Swagger documentation for all endpoints
- Fully testable using Postman or similar API tools

---

### Requirements

- Django, Django REST Framework
- MySQL (configured as in previous milestones)
- drf-yasg for Swagger docs
- Project setup and migrations completed

---

### Getting Started

1. Clone the repository and navigate to the project directory.
2. Install dependencies (if not already done):
   ```bash
   pip install -r requirements.txt
   ```
3. Apply migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```
5. Use Postman to test the API endpoints for listings and bookings under `/api/` (CRUD: GET, POST, PUT, DELETE).
6. View API documentation at [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

---

### Structure

- `listings/views.py` — ViewSets for `Listing` and `Booking`
- `listings/urls.py` — API routing using DRF routers
- `README.md` — This file

---

**Repository structured and maintained according to ALX guidelines.**