# 📝 Blog API with Django & DRF

A simple RESTful API for a blog platform, built with Django and Django REST Framework (DRF).  
Supports creating, reading, updating, and deleting posts and comments, with authenticated user authorship and full test coverage.

---

## 🚀 Features

- CRUD operations for blog posts
- Nested comments per post
- Authenticated authorship (each post and comment belongs to a user)
- Token-based authentication (JWT-ready)
- Automated tests with coverage tracking
- Clean modular Django project structure

---

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (for development)
- `pytest` and `coverage` for testing

---

## 📦 Setup Instructions

### 1. Clone and create virtual environment:

```bash
git clone https://github.com/dpensky/blog-api.git
cd blog-api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run migrations:
```bash
python manage.py migrate
```

### 4. Create a superuser (optional for admin access):
```bash
python manage.py createsuperuser
```

### 5. Start the development server:
```bash
python manage.py runserver
```
[Swagger UI](http://localhost:8000/swagger/)  
[ReDoc UI](http://localhost:8000/redoc/)

## 🧪 Running Tests
```bash
coverage run manage.py test
coverage report
```

--

## 🧰 API Endpoints (Examples)
```text
Method  Endpoint                        Description
GET	    /posts/                         List all posts
POST    /posts/                         Create a new post
GET	    /posts/<id>/                    Retrieve a single post
PUT	    /posts/<id>/                    Update a post (author only)
DELETE  /posts/<id>/                    Delete a post (author only)
GET	    /posts/<id>/comments/           List comments for a post
POST    /posts/<id>/comments/create/    Create a comment (auth user)
```

⚠️ All POST, PUT, and DELETE requests require authentication.

--

## 📄 Authentication
The project supports token authentication and is compatible with JWT if desired. You can add djangorestframework-simplejwt for JWT-based login/logout.

---

## 📌 TODO / Future Improvements
[ ] Add authentication
[ ] Add permissions (e.g., only authors can edit/delete their content)
[ ] Pagination and search for posts
[ ] Like system or post categories
[X] Swagger/OpenAPI documentation
[ ] Docker support

---

## 🧑‍💻 Author
Darcio Pensky  
[LinkedIn](https://www.linkedin.com/in/dpensky/)  
[GitHub](https://github.com/dpensky)  

---

# 📜 License
MIT
