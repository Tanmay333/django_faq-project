# Django FAQ Management System 
## Project Overview

This is a Django-based FAQ Management System that allows users to create, read, update, and delete frequently asked questions (FAQs). The system supports multilingual translations using the Google Translate API and implements caching using Redis for optimized performance.

## Features

CRUD Operations: Create, Read, Update, and Delete FAQs.

Multilingual Support: FAQs can be automatically translated into different languages.

REST API: Built using Django REST Framework.

Caching: Uses Redis to store translated FAQs and improve performance.

Admin Panel: Manage FAQs from Django's built-in admin interface.

## Folder Structure
faq/                # Core Django app

faq_app/            # Main application with models, views, serializers, and URLs

faq_project/        # Django project settings and configurations

.gitignore          # Git ignore file (ignores venv, DB, and unnecessary files)

manage.py           # Django project management script

## 🚀 Getting Started

**Clone the Repository**
``` git clone https://github.com/Tanmay333/django_faq-project.git
cd django_faq-project

 ```
**Create and Activate Virtual Environment**
``` python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows

```
**Install Dependencies**
```
 pip install -r requirements.txt

```
**Run Migrations**
```
 python manage.py migrate

```
**Start the Development Server**
```
 python manage.py runserver

```
**Base URL**
http://127.0.0.1:8000/

## Environment Variables (Set in .env) 
```GOOGLE_TRANSLATE_API_KEY=your_api_key_here
REDIS_URL=redis://localhost:6379

```
 Happy Coding! If you have any issues, feel free to contribute or open an issue
