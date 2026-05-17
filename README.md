# Tech Stack & Libraries

* Framework: Flask (Python)
* Database: SQLite (SQLAlchemy ORM)
* Forms: Flask-WTF (with CSRF protection)
* Authentication: Flask-Login
* Admin Panel: Flask-Admin
* Styling: Bootstrap 5 (HTML/CSS)

---

# Setup Instructions

Please follow the steps below to run the application locally.

## Step 1: Create & Activate Virtual Environment

### For macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### For Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 3: Initialize Database

Run the setup script to create the database schema and default administrator account.

```bash
python3 setup_db.py
```

### Default Admin Credentials

* Email: [admin@problog.com](mailto:admin@problog.com)
* Password: Admin123!

## Step 4: Run the Application

```bash
python3 run.py
```

---

# Project Overview

The Simple Blog Application is a multi-user blogging platform designed for structured content management with secure authentication and role-based access control.

The project follows a modular Flask architecture using Blueprints and the Factory Pattern to ensure scalability, maintainability, and clean code organization.

---

# Application Features

## 1. Tiered Access Control

### Guest Users

* View blog posts
* Read post details

### Authenticated Users

* Create blog posts
* Edit their own posts
* Delete their own posts

### Administrators

* Moderate all blog content
* Access admin dashboard
* Manage users and posts

---

## 2. Blog Post Management (CRUD)

### Features

* Create new posts
* Read/View all posts
* Update/Edit existing posts
* Delete posts

### Blog Post Fields

* Title
* Content Body
* Author Information
* Created Timestamp
* Updated Timestamp

---

## 3. Secure Authentication System

The application implements:

* Password hashing using Werkzeug
* Session management using Flask-Login
* CSRF protection using Flask-WTF
* Protected routes for authenticated users
* Persistent login sessions

---

## 4. Responsive User Interface

* Mobile-first responsive design
* Bootstrap 5 based UI
* Chronological blog feed
* Clean and user-friendly navigation

---

# 📚 Libraries & Technical Justification

## Flask

Flask was selected due to its lightweight and modular architecture. It supports Blueprints and the Factory Pattern, making the application scalable and maintainable.

## Flask-SQLAlchemy

SQLAlchemy ORM abstracts the database layer and enables migration from SQLite (development) to PostgreSQL/MySQL (production) without major code changes.

## Flask-Login

Flask-Login simplifies user authentication and session management, including login persistence and route protection.

## Flask-WTF & WTForms

Used for secure form handling with:

* CSRF protection
* Server-side validation
* Cleaner form management

## Werkzeug Security

Werkzeug provides secure password hashing using PBKDF2 with salting, ensuring passwords remain protected even in case of database exposure.

## Flask-Admin

Flask-Admin provides an administrative dashboard for:

* Managing users
* Managing blog posts
* Administrative tasks

---

# Security Features

* CSRF Protection
* Password Hashing
* Session Management
* Route Authorization
* Secure Form Validation

---

# Architecture Highlights

The project follows:

* Modular Flask Architecture
* Blueprint-Based Routing
* Factory Pattern
* ORM-Based Database Management
* Separation of Concerns

### Benefits

* Scalability
* Code Maintainability
* Reusability
* Easier Testing


