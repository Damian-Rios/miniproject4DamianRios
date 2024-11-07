### INF601 - Advanced Programming in Python
### Damian Rios
### Mini Project 4


# Mini Project 4 - Expense Tracker


## Description
**Expense Tracker** is a web application developed using Django that allows users to manage and track their personal expenses. The app features user authentication, where users can register, log in, and securely manage their expenses. Users can add, edit, and delete their expense records.

The application uses Bootstrap for a responsive design, ensuring it works well on both desktop and mobile devices.

## Getting Started
To set up the project locally, follow the instructions below.

### Prerequisites
- Python 3.x installed on your machine.
- A virtual environment (recommended) to manage dependencies.

### Dependencies
Make sure all required libraries are installed by running:
```
pip install -r requirements.txt
```

### Executing the Program
1. **Clone the repository:**
https://github.com/Damian-Rios/miniproject4DamianRios.git

2. **Create a virtual environment:**
```
python -m venv venv
```
Then activate the virtual environment:
- On macOS/Linux:
```
source venv/bin/activate
```
- On Windows use 
```
venv\Scripts\activate
```

3. **Install the dependencies:**

4. Create migrations (if necessary):
To ensure that your database schema is up-to-date, run the following command to create migration files:
```
python manage.py makemigrations
```

5. **Run migrations:**
Run the following command to apply the database migrations:
```
python manage.py migrate
```

6. **Create a superuser (optional):**
If you want to access the Django admin panel, create a superuser by running:
```
python manage.py createsuperuser
```

7. **Run the application:**
Start the development server by running:
```
python manage.py runserver
```

8. **Access the application:**
After running the application, you can access it by navigating to the following URL in your browser:
`http://127.0.0.1:8000`

   
### Output
The application allows users to manage their personal finances. Users can:
- Register, log in, and securely manage their account.
- Add, edit, and delete expenses, each with a category, description, and amount.
- Access an admin panel (if you created a superuser) to manage users and expenses.


## Authors
Damian Rios


## Acknowledgments
Inspiration, code snippets, etc.
* [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
* [Django Tutorial](https://docs.djangoproject.com/en/4.2/intro/)
* [Django Documentation](https://docs.djangoproject.com/en/4.2/)