# 💰 Expense Tracker REST API

A REST API built with Django REST Framework for tracking personal expenses.

## Features

- ✅ User authentication
- ✅ CRUD for expenses and categories
- ✅ Filter by category, min/max amount
- ✅ Search by title or notes
- ✅ Summary endpoint with totals per category

## Tech Stack

- **Backend**: Python, Django
- **API**: Django REST Framework
- **Database**: SQLite

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/expenses/` | List & create expenses |
| GET/PUT/DELETE | `/api/expenses/{id}/` | Retrieve, update, delete |
| GET | `/api/expenses/summary/` | Total per category |
| GET/POST | `/api/categories/` | List & create categories |

## Installation

```bash
git clone https://github.com/hlias2312/expense-tracker-api.git
cd expense-tracker-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```