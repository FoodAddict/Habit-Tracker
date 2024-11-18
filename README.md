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
