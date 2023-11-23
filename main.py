from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SelectField, DateField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Simulated user data and asset data (replace with a database in a real application)
users = [
    {'username': 'your-username', 'password': 'your-password'},
    {'username': 'user2', 'password': 'password2'}
]

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class AssetForm(FlaskForm):
    action = SelectField('Action', choices=[('issue', 'Issue'), ('return', 'Return')], validators=[DataRequired()])
    date = DateField('Date', validators=[DataRequired()])
    employee_name = StringField('Employee Name', validators=[DataRequired()])
    asset_type = StringField('Asset Type', validators=[DataRequired()])
    laptop = StringField('Laptop', validators=[DataRequired()])
    bag = StringField('Bag', validators=[DataRequired()])
    headset = StringField('Headset', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        # Process the form data (in a real application, you'd likely validate against a database)
        username = form.username.data
        password = form.password.data

        # Check if the provided username and password match any user in the simulated data
        if any(user['username'] == username and user['password'] == password for user in users):
            # Redirect to the dashboard upon successful login
            return redirect(url_for('dashboard'))

    return render_template('login.html', form=form)

@app.route('/validate_login', methods=['POST'])
def validate_login():
    form = LoginForm()

    if form.validate_on_submit():
        # Process the form data (in a real application, you'd likely validate against a database)
        username = form.username.data
        password = form.password.data

        # Check if the provided username and password match any user in the simulated data
        if any(user['username'] == username and user['password'] == password for user in users):
            # Redirect to the dashboard upon successful login
            return redirect(url_for('dashboard'))

    # Handle validation errors by rendering the login page with the form
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    form = AssetForm()

    if form.validate_on_submit():
        # Process the form data (in a real application, you'd likely store this in a database)
        action = form.action.data
        date = form.date.data
        employee_name = form.employee_name.data
        asset_type = form.asset_type.data
        laptop = form.laptop.data
        bag = form.bag.data
        headset = form.headset.data
        # Retrieve more fields as needed

        # Redirect to a success page or back to the dashboard
        return redirect(url_for('dashboard'))

    return render_template('dashboard.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
