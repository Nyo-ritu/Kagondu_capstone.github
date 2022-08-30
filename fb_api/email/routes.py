from flask import Flask, render_template, request, flash, Blueprint, redirect
from fb_api.forms import ContactForm
from flask.helpers import url_for
from flask_mail import Mail, Message
from flask_mail import Mail, Message
import os

from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)

cont = Blueprint('cont', __name__, template_folder='contact_templates')

Email_Addr = os.getenv('Email_Addr')
Email_Pass = os.getenv('Email_Pass')

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": os.environ['Email_Addr'],
    "MAIL_PASSWORD": os.environ['Email_Pass']
}

app.config.update(mail_settings)
mail = Mail(app)

@cont.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        with app.app_context():
            msg = Message(subject=form.email.data,
                      sender=form.name.data,
                      recipients=['testapps986@gmail.com'], 
                      body=form.message.data)
            mail.send(msg)
      
        flash(f'Thank you for your input!', 'auth-success')
        return redirect(url_for('site.home'))
      
    elif request.method == 'POST' and form.validate_on_submit() == False:
        flash(f'Please enter a valid email.', 'auth-fail')
    return render_template('contact.html', form=form)
    

    
