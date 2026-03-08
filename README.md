# Clinic Inventory & Medicine Management System

## 1. Project Overview

The Clinic Inventory & Medicine Management System is a web-based application developed to help clinics efficiently manage their medicine inventory. The system allows administrators to store medicine details, monitor stock levels, track expiry dates, and manage inventory records.

This system helps reduce manual work and improves the efficiency of medicine stock management in clinics.

Main features include:

* Medicine inventory management
* Add, edit, and delete medicine records
* Low stock alert system
* Expiry date monitoring
* Search medicines by name
* Dashboard displaying inventory statistics

---

## 2. Technology Stack Used

Frontend:

* HTML
* CSS
* Bootstrap

Backend:

* Python
* Django Framework

Database:

* SQLite (Default Django database)

Development Tools:

* Git
* GitHub
* PythonAnywhere (for deployment)

---

## 3. Installation and Setup Steps

Follow these steps to run the project locally.

### Step 1: Clone the Repository

git clone https://github.com/yourusername/clinic-inventory-system.git

### Step 2: Navigate to the Project Folder

cd clinic-inventory-system

### Step 3: Create Virtual Environment

python -m venv env

### Step 4: Activate Virtual Environment

Windows:
env\Scripts\activate

Linux/Mac:
source env/bin/activate

### Step 5: Install Dependencies

pip install -r requirements.txt

### Step 6: Apply Database Migrations

python manage.py migrate

### Step 7: Create Admin User

python manage.py createsuperuser

### Step 8: Run the Development Server

python manage.py runserver

Open browser and visit:
http://127.0.0.1:8000/

---

## 4. Database Configuration

The application uses SQLite as the default database provided by Django.

Database settings are configured in the `settings.py` file.

Example configuration:

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.sqlite3',
'NAME': BASE_DIR / 'db.sqlite3',
}
}

---

## 5. Application Routes / URLs

Main routes used in the system:

| URL              | Description           |
| ---------------- | --------------------- |
| /                | Dashboard             |
| /medicine_table/ | View all medicines    |
| /add/            | Add new medicine      |
| /edit/<id>/      | Edit medicine         |
| /delete/<id>/    | Delete medicine       |
| /details/<id>/   | View medicine details |

---

## 6. Assumptions Made During Development

* Only the admin can add, update, or delete medicines.
* Users can only view medicine information.
* Low stock warning is triggered when stock is less than 10.
* Medicines nearing expiry are highlighted for easier monitoring.
* The system is designed for small clinics and pharmacy inventory management.
---

## 7. Author
Project Developed By:
Safwan
Project Developed By:
Safwan
