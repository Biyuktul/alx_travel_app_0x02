# alx_travel_app_0x00

## Milestone 2: Creating Models, Serializers, and Seeders

This milestone expands the backend foundation by defining the core data models, setting up serializers for API representation, and implementing data seeding for development and testing.

---

### Project Overview

This repository covers database modeling, serialization, and data seeding for the Django-based travel listing platform. The focus is on building robust and relational models, enabling API-ready data structures, and providing tools to populate the system with initial data.

---

### Key Features

- Database models for `Listing`, `Booking`, and `Review` in `listings/models.py`
- Serializers for `Listing` and `Booking` in `listings/serializers.py`
- Custom Django management command for seeding sample listings data:  
  `listings/management/commands/seed.py`
- All models designed with appropriate fields, relationships, and constraints

---

### Requirements

- Django, Django REST Framework
- MySQL (as configured in Milestone 1)
- Environment variables handled via `django-environ`
- Project cloned and set up as per previous milestone

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
4. Seed the database with sample listings:
   ```bash
   python manage.py seed
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```
6. Use Postman to test the API endpoints for listings and bookings.

---

### Structure

- `listings/models.py` — Contains `Listing`, `Booking`, and `Review` models
- `listings/serializers.py` — Serializers for API data representation
- `listings/management/commands/seed.py` — Seeder command for populating sample data

---

**Repository structured and maintained according to ALX guidelines.**
