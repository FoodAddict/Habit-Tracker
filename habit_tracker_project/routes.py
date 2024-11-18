from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import db, User, Habit
from flask_bcrypt import Bcrypt
from flask_login import login_user, logout_user, login_required, current_user, LoginManager
import re
import html
from datetime import datetime, timedelta


main_blueprint = Blueprint('main', __name__)
login_manager = LoginManager()
login_manager.login_view = 'main.login'

@main_blueprint.route('/')
def index():
    return render_template('index.html', title="Home")

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def sanitize_input(input_text):
    """Sanitize input to prevent XSS and other unwanted injections."""
    return html.escape(input_text.strip())

@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = sanitize_input(request.form.get('username'))
        email = sanitize_input(request.form.get('email'))
        password = sanitize_input(request.form.get('password'))

        # Check if the email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already exists. Please choose a different email.', 'danger')
            return redirect(url_for('main.register'))

        if not re.match(r"^[a-zA-Z0-9_]+$", username):
            flash('Invalid username. Use letters, numbers, and underscores only.', 'danger')
            return redirect(url_for('main.register'))

        hashed_password = Bcrypt().generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title="Register")

@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = sanitize_input(request.form.get('email'))
        password = sanitize_input(request.form.get('password'))
        user = User.query.filter_by(email=email).first()
        if user:
            if Bcrypt().check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('main.dashboard'))
            else:
                flash('Incorrect password. Please try again.', 'danger')
        else:
            flash('Email does not exist. Please register first.', 'danger')
    return render_template('login.html', title="Login")

@main_blueprint.route('/dashboard')
@login_required
def dashboard():
    habits = Habit.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', habits=habits, title="Dashboard")

@main_blueprint.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.login'))

@main_blueprint.route('/add_habit', methods=['POST'])
@login_required
def add_habit():
    habit_name = sanitize_input(request.form.get('name'))
    if habit_name:
        new_habit = Habit(name=habit_name, owner=current_user)
        db.session.add(new_habit)
        db.session.commit()
        flash('Habit added successfully!', 'success')
    else:
        flash('Habit name cannot be empty.', 'danger')
    return redirect(url_for('main.dashboard'))

@main_blueprint.route('/delete_habit/<int:habit_id>', methods=['POST'])
@login_required
def delete_habit(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    if habit.owner == current_user:
        db.session.delete(habit)
        db.session.commit()
        flash('Habit deleted successfully!', 'success')
    else:
        flash('You do not have permission to delete this habit.', 'danger')
    return redirect(url_for('main.dashboard'))


@main_blueprint.route('/check_in/<int:habit_id>', methods=['POST'])
@login_required
def check_in(habit_id):
    habit = Habit.query.get_or_404(habit_id)
    if habit.owner != current_user:
        flash('You do not have permission to check in for this habit.', 'danger')
        return redirect(url_for('main.dashboard'))

    current_time = datetime.now()
    if habit.last_check_in is None or (current_time - habit.last_check_in).days >= 1:
        habit.streak += 1
        habit.last_check_in = current_time
        db.session.commit()
        flash('Check-in successful! Your streak has been updated.', 'success')
    else:
        flash('You have already checked in today. Please come back tomorrow.', 'info')

    return redirect(url_for('main.dashboard'))
