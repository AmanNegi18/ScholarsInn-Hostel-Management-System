Hostel Management System (Django)

Scholars Inn is a web-based Hostel Management System built using Django.
It helps manage hostels, rooms, students, mess menus, and notices through an easy-to-use web interface.
User authentication (Student login)
Hostel and room management
Student registration and profile management
Mess menu management (breakfast, lunch, dinner)
Notice board for announcements
Admin panel for managing data
Responsive UI using Django templates and static files
scholarsinnn12/
│
├── hostel/                 # Main application
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── scholarsinnn/            # Project settings
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│
├── templates/               # HTML templates
├── static/                  # CSS files
├── db.sqlite3               # Database
└── manage.py

Clone the Repository
git clone https://github.com/your-username/scholars-inn.git
cd scholars-inn
Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Install Dependencies
pip install django
Run Database Migrations
python manage.py migrate
Create Superuser
python manage.py createsuperuser
Run the Development Server
python manage.py runserver
Now open your browser and go to:
http://127.0.0.1:8000/
Admin panel:
http://127.0.0.1:8000/admin/
