from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Here, you can perform any authentication logic
        # For simplicity, let's redirect to a success page
        return redirect(url_for('success'))
    return render_template('login.html', form=form)

@app.route('/success')
def success():
    return "Login Successful!"

if __name__ == '__main__':
    app.run(debug=True)
