from flask import Flask, render_template, request, flash, Blueprint, redirect
from fb_api.forms import ContactForm
from flask.helpers import url_for



cont = Blueprint('cont', __name__, template_folder='contact_templates')

@cont.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
      
        flash(f'Thank you for your input!', 'auth-success')
        return redirect(url_for('site.home'))
      
    elif request.method == 'POST' and form.validate_on_submit() == False:
        flash(f'Please enter a valid email.', 'auth-fail')
    return render_template('contact.html', form=form)
    

    
