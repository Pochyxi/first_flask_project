# flask-wtf ---> per creare i form su flask
# pip install flask_wtf
# pip install wtforms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='Nome Utente:')
    email_address = StringField(label='Email:')
    password1 = PasswordField(label='Password:')
    password2 = PasswordField(label='Conferma Password:')
    submit = SubmitField(label='Crea il tuo account')
    