# Django JWT Login System with Firm Management

This project is a login system built using Django and Django REST Framework. It uses JWT tokens for authentication and lets users register, log in, and manage multiple firms. The frontend is made with HTML, Bootstrap, and JavaScript (using `fetch()` instead of Axios).

---

## 📁 Project Structure

    Here's a quick idea of how things are organized:
    login_system/
    ├── core/                      # Main app (models, views, serializers, templates)
    │   ├── models.py             # User and Firm models
    │   ├── serializers.py        # DRF serializers
    │   ├── views.py              # API views and HTML render views
    │   ├── urls.py               # App-specific URL routes
    │   └── templates/
    │       └── core/
    │           ├── register.html
    │           ├── login.html
    │           └── dashboard.html
    ├── login_system/
    │   ├── settings.py           # Project settings (auth, middleware, installed apps)
    │   └── urls.py               # Root URL config
    ├── db.sqlite3                # SQLite database
    ├── manage.py                 # Django's CLI tool
    ├── requirements.txt          # Python dependencies
    └── README.md                 # Project documentation

---

## 🧰 Tech Stack

Here’s what the project uses:

- **Python 3.10+**
- **Django 4+**
- **Django REST Framework**
- **SimpleJWT** for authentication
- **SQLite** (for now, simple and local)
- **Bootstrap 5** for UI
- **JavaScript** for API requests
- **Postman** was used for testing the backend before integrating frontend

No React or heavy frontend frameworks. Just basic and functional.

---

## ✅ What This Project Does

You can:

- Register as a user
- Log in and receive access/refresh tokens
- Store those tokens in localStorage
- See a user dashboard after login
- Create, update, or delete firms tied to your account
- Update your own user info
- Delete your user account

Admins can use the Django admin panel to see all users and firms.

---

## 🔌 API Overview

These are the API endpoints the frontend uses:

### Auth

| Method | Endpoint           | Purpose                  |
|--------|--------------------|--------------------------|
| POST   | `/api/register/`   | Register new user        |
| POST   | `/token/`          | Get access + refresh     |
| POST   | `/token/refresh/`  | Refresh access token     |

### Users

| Method | Endpoint         | Purpose                  |
|--------|------------------|--------------------------|
| GET    | `/user/`         | Get current user         |
| PATCH  | `/user/<id>/`    | Update username/email    |
| DELETE | `/user/<id>/`    | Delete user account      |

### Firms

| Method | Endpoint         | Purpose                  |
|--------|------------------|--------------------------|
| GET    | `/firms/`        | List firms of a user     |
| POST   | `/firms/`        | Add a new firm           |
| PATCH  | `/firms/<id>/`   | Update firm details      |
| DELETE | `/firms/<id>/`   | Delete a firm            |

---

## 🌐 Frontend Routes

These are just plain HTML files rendered through Django.

| Page        | URL            | Description               |
|-------------|----------------|---------------------------|
| Register    | `/register/`   | New user registration     |
| Login       | `/login/`      | Login and token fetch     |
| Dashboard   | `/dashboard/`  | View firms and actions    |

All frontend logic uses `fetch()` to send/receive data from the API.

---
## Install dependencies
 
 ```bash
pip install -r requirements.txt
 ```

## Apply Migrations

 ```bash
python manage.py makemigrations
python manage.py migrate
 ```

## Create superuser (for admin panel)

 ```bash
python manage.py createsuperuser
 ```

## Run the development server

```bash
python manage.py runserver
 ```

## Visit these in browser

```bash
http://127.0.0.1:8000/register/

http://127.0.0.1:8000/login/

http://127.0.0.1:8000/dashboard/

http://127.0.0.1:8000/admin/ (for admin access)
```

## 🧾 requirements.txt

```bash
Django>=4.2
djangorestframework>=3.14
djangorestframework-simplejwt
```

## 🔐 Notes

- Token is stored in browser localStorage  
- CSRF is skipped for API-only views (since we're using fetch)  
- Admin panel uses default Django UI  
- All templates are inside `core/templates/core`![multiple_firms](https://github.com/user-attachments/assets/d817eed7-3a70-4c9f-818d-8d0b869e8c6f)
![update](https://github.com/user-attachments/assets/dbbf2e52-3bd9-4447-ad01-71a691b01254)
![dashboard_2](https://github.com/user-attachments/assets/7a3bdc3e-4203-4b8b-8e46-7bf45f99b3b2)
![dashboard_1](https://github.com/user-attachments/assets/78ee62a6-eddb-4115-88ed-07b047cd5939)
![login](https://github.com/user-attachments/assets/322f8592-73cf-46cf-a2a5-e1bce076f322)
![register](https://github.com/user-attachments/assets/92e8b572-f0fa-4abc-b1fe-02d93e9ba7c3)
![PostMan](https://github.com/user-attachments/assets/10f1e520-a543-412b-85b4-ab146e0b0221)
