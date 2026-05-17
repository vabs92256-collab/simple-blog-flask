# Professional Flask Blog Application

A modular, secure, and feature-rich Blog Management System built with Python and the Flask web framework. This application allows users to create and manage personal blog posts while providing administrators with a powerful dashboard for site oversight.

##  Features

### 1. User Authentication & Security
- **Secure Sign-Up & Login:** Integrated account management using `Flask-Login`.
- **Password Hashing:** Industry-standard security using `Werkzeug` (PBKDF2) to ensure passwords are never stored in plain text.
- **Session Management:** Protected routes that redirect unauthorized users to the login page.

### 2. Blog Management (CRUD)
- **Full Lifecycle:** Users can Create, Read, Update, and Delete their own posts.
- **Data Integrity:** Each post tracks Title, Body, and a Timestamp.
- **Ownership Protection:** Back-end logic ensures users can only modify content they personally created.

### 3. Professional UI/UX
- **Landing Page:** A clean, reverse-chronological feed of all blog posts.
- **Detail View:** Dedicated pages for reading full articles.
- **Responsive Design:** Built with **Bootstrap 5**, ensuring the application works on desktops, tablets, and mobile devices.

### 4. Administrative Dashboard
- **Flask-Admin Integration:** A secure "Mode" interface located at `/admin`.
- **Global Control:** Admins can manage all users and moderate all posts from a central dashboard.

---

## 🛠️ Tech Stack & Libraries

- **Framework:** Flask (Python)
- **Database:** SQLite (SQLAlchemy ORM)
- **Forms:** Flask-WTF (with CSRF protection)
- **Auth:** Flask-Login
- **Admin:** Flask-Admin
- **Styling:** Bootstrap 5 (HTML/CSS)

---

## Setup 

Follow these steps to set up the environment and run the application locally.

### 1. Clone the Repository
```bash
git clone <your-repository-link>
cd flask_app_datagrid