# 📝 To-Do List Application

A simple, beginner-friendly to-do list application built using Django. This app allows users to manage tasks through a clean interface, supporting creation, completion, and deletion of tasks.

## 🚀 Features

- ✅ Add new tasks
- ❌ Delete tasks
- ☑️ Mark tasks as completed
- 📋 View all tasks

## 🛠️ Technologies Used

- Python 3
- Django 5
- HTML5
- CSS3

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/MehradVol4/to-do-list.git
   cd to-do-list
2.Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3.Install dependencies

pip install -r requirements.txt
Run database migrations

python manage.py migrate
Start the development server


python manage.py runserver
Open in browser

Visit: http://127.0.0.1:8000

📁 Project Structure
css
Copy
Edit
to-do-list/
├── main/
│   ├── migrations/
│   ├── templates/
│   │   └── main/
│   │       └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── todolist/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
└── manage.py
