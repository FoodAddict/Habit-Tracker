# Habit Tracker Project

Welcome to the **Habit Tracker** project! This is a web application designed to help users track their habits, build positive routines, and provide valuable strategies for forming lasting habits.

## Project Overview

The Habit Tracker is built using Flask and provides features such as user authentication, habit management, daily check-ins, and a reset mechanism for streaks. The project also offers educational content on habit formation and strategies to maintain habits over time.

### Key Features

- User registration and login system with secure password storage.
- Dashboard for users to manage their habits, track streaks, and perform daily check-ins.
- Habit management system with functionality to add, delete, and track streaks.
- Flash messaging for real-time feedback (e.g., on user actions such as login failures, habit updates).
- Educational content about building and maintaining habits.

## Project Structure

```plaintext
Habit-Tracker/
├── app.py              # Main application file
├── config.py           # Configuration file
├── models.py           # Database models
├── routes.py           # Routes and view logic
├── templates/          # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   └── dashboard.html
└── static/             # Static files (CSS, JS)
    └── style.css

```

## Prerequisites

To run the Habit Tracker application, you need to have the following installed on your system:

- [Python 3.6+](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/)
- [Virtualenv](https://virtualenv.pypa.io/)

## Installation Guide

1. **Clone the repository**

   ```bash
   git clone https://github.com/FoodAddict/Habit-Tracker.git
   cd Habit-Tracker
   ```
2. **Create a virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```
4. **Configure the Application**
    Ensure that config.py contains the necessary configuration settings, including a SECRET_KEY for session management and a database URI (e.g., SQLite for local development).

5. ** Init Database**
   Enter Python Enviroment
    ```bash
    python3
    ```
    Run Script
    ```bash
    from app import create_app, db
    app = create_app()
    with app.app_context():
        db.create_all()
    ```
    Exit Python Enviroment
   ```bash
   exit()
   ```

6. **Run Application**
    ```bash
    python3 app.py
    ```
7. **Access Application**
    Open your web browser and go to http://127.0.0.1:5000/ to view the application.
   
## Project Features and Usage
1. **User Authentication**
    Registration: Users can create a new account by providing a username, email, and password.
    Login: Existing users can log in using their email and password.
    Logout: Authenticated users can log out of their accounts.
2. **Habit Management Dashboard**
    Add Habits: Users can add new habits to track.
    Delete Habits: Users can delete existing habits.
    Track Streaks: Users can check in daily to maintain and track their habit streaks.
3. **Habit Tips and Strategies **
    Learn about proven strategies and tips for building lasting habits through dedicated content on the homepage.

   
### Important Routes
```bash
/ - Homepage with habit strategies and tips.
/register - User registration page.
/login - User login page.
/dashboard - User-specific dashboard for habit management (requires login).
```
## Troubleshooting
**404 Errors**
    Ensure you have registered all blueprints correctly and that the route definitions are accurate.
    Double-check that index.html and other templates are located in the templates directory.
    
**Database Issues**
    Ensure you have run db.create_all() in the correct context.
    Verify that your database URI is correctly configured in config.py.
    Styling Issues
    Ensure that style.css is correctly linked in base.html.

### Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

### License
This project is open-source and available under the MIT License.
