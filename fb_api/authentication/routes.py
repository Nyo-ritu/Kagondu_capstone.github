from flask import Blueprint, render_template, request, redirect, flash
from flask.helpers import url_for
from fb_api.forms import UserLoginForm
from fb_api.models import db, User, check_password_hash
from werkzeug.security import generate_password_hash

from flask_login import login_user, logout_user, login_required


auth = Blueprint('auth', __name__, template_folder='auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            email = form.email.data
            password = form.password.data
            print(email, password)
            new_user = User(email, password)
            db.session.add(new_user)
            db.session.commit()
            flash(f'Your email account ({email}) has been successfully created!', 'create-success')
            return redirect(url_for('auth.signin'))
        flash(f'A user already exists with that email address, please try again', 'auth-nogood')
    elif request.method == 'POST' and form.validate_on_submit() == False:
        flash(f'Please enter a valid email', 'auth-fail')
    return render_template('signup.html', form = form)

@auth.route('/signin', methods=['GET','POST'])
def signin():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(email, password)
        logged_user = User.query.filter(User.email == email).first()
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            flash(f'You are now logged in as {email}', 'auth-success')
            return redirect(url_for('site.home'))
        else:
            flash(f'Incorrect email/password, please try again.', 'auth-fail')
            return redirect(url_for('auth.signin'))
    elif request.method == 'POST' and form.validate_on_submit() == False:
        flash(f'Please enter a valid email', 'auth-fail')
    return render_template('signin.html', form = form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash(f'You have successfully logged out.', 'auth-success')
    return redirect(url_for('site.home'))



