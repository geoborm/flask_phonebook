from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import SignUpForm

@app.route('/')
def index():
    return render_template('index.html', name = 'Geoff')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    # Create an instance of the form (in the context of the current request)
    form = SignUpForm()
    # Check if the form was submitted and that all of the fields are valid
    if form.validate_on_submit():
        # If so, get the data from the form fields
        print('Hooray our form was validated!!')
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        email = form.email.data
        address = form.address.data
        print(first_name, last_name, phone_number, email, address)
        flash(f"Thank you {first_name} for signing up!", "success")
        return redirect(url_for('index'))
    return render_template('signup.html', form=form)