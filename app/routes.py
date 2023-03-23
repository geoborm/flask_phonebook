from app import app
from flask import render_template, redirect, url_for, flash
from app.forms import PhoneForm

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add-phone', methods=["GET", "POST"])
def add_phone():
    form = PhoneForm()
    # Check if the form was submitted and is valid
    if form.validate_on_submit():
        first = form.first_name.data
        last = form.last_name.data
        address = form.address.data
        phone = form.phone_number.data
        print(first, last, address, phone)
        flash(f"{first} {last} has been added to the phone book", "success")
        return redirect(url_for('index'))
    return render_template('add_phone.html', form=form)