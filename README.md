# Django CSV Data Management Readme

## Table of Contents
1. Project Overview
2. Features
3. Installation
4. Usage
5. File Structure
6. Dependencies

## 1. Project Overview
This Django project is designed for managing and analyzing CSV data. It includes features for user authentication, CSV data upload, user management, and a data query builder. Below is an overview of the project's structure and functionality.

## 2. Features
### 2.1. User Authentication
- Users can log in using their credentials.
- Authentication ensures secure access to data management features.

### 2.2. CSV Data Upload
- Authenticated users can upload CSV files.
- The uploaded CSV data is processed and stored in the database.

### 2.3. User Management
- Users can view a list of registered users.
- Admin users can add new users to the system.

### 2.4. Data Query Builder
- Users can perform advanced searches on the uploaded CSV data.
- Search parameters include keywords, industry, year founded, locality, country, and employee count ranges.

### 2.5. Data Deletion
- Users with appropriate permissions can delete all data records.

## 3. Installation
To run this project locally, follow these steps:
1. Clone the project repository.
2. Create a virtual environment and activate it.
3. Install the project dependencies using `pip install -r requirements.txt`.
4. Set up your database settings in the project's `settings.py`.
5. Run the database migrations using `python manage.py migrate`.
6. Create a superuser using `python manage.py createsuperuser` to access the admin panel.
7. Start the development server with `python manage.py runserver`.

## 4. Usage
1. Access the web application in your browser.
2. Log in with your credentials or create a new account.
3. Upload CSV data files.
4. View and manage user data records.
5. Use the data query builder to perform advanced searches.
6. Delete all data records when necessary.

## 5. File Structure
- **`manage.py`**: Django management script.
- **`your_project/`**: Main project directory.
  - **`settings.py`**: Project settings, including database configuration and installed apps.
  - **`urls.py`**: URL routing for the project.
  - **`templates/`**: HTML templates for rendering web pages.
  - **`models.py`**: Django models defining the database schema.
  - **`forms.py`**: Forms for user input validation.
  - **`views.py`**: Views defining the project's functionality.
  - **`static/`**: Static files (CSS, JavaScript) for the web application.
- **`requirements.txt`**: List of project dependencies.

## 6. Dependencies
- Django: Web framework for building web applications.
- pandas: Library for data manipulation and CSV file handling.
- psycopg2-binary: PostgreSQL database adapter.
- django-crispy-forms: Library for styling Django forms.
- gunicorn (optional): A WSGI HTTP server for production deployment.

Please ensure you have these dependencies installed in your virtual environment before running the project.

This readme provides an overview of the Django CSV data management project. For more detailed documentation and customization, refer to the Django official documentation and other relevant packages used in the project.
