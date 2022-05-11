from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *

class login_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),
        #validators.Email()
    ], description="You need an email address to sign in!")

    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35)
    ],description="You need a password to sign in!")
    submit = SubmitField()

class register_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),
        #validators.Email()
    ], description="You need an email address to sign up!")

    password = PasswordField('Create Password', [
        validators.DataRequired(),
        #validators.length(min=6, max=35),
        validators.EqualTo('confirm', message='Passwords must match')
    ], description="Create a password.")
    confirm = PasswordField('Repeat Password', description="Please confirm your password.")
    submit = SubmitField()

class create_user_form(FlaskForm):
    email = EmailField('Email Address', [validators.DataRequired()], description="You need to signup with an email")

    password = PasswordField('Create Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
    ], description="Create a password.")

    confirm = PasswordField('Repeat Password', description="Please retype your password to confirm it is correct")
    is_admin = BooleanField('Admin', render_kw={'value':'1'})
    submit = SubmitField()

class profile_form(FlaskForm):
    about = TextAreaField('About', [validators.length(min=6, max=300)], description="Tell us about yourself")
    submit = SubmitField()

class user_edit_form(FlaskForm):
    about = TextAreaField('About', [validators.length(min=6, max=300)], description="Tell us about yourself")
    is_admin = BooleanField('Admin', render_kw={'value':'1'})
    submit = SubmitField()

class security_form(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),
        #validators.Email()
    ], description="Change your email address")

    password = PasswordField('Create Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match'),
        #validators.length(min=6, max=35)
    ], description="Create a password")
    confirm = PasswordField('Repeat Password', description="Please retype your password to confirm it is correct")
    submit = SubmitField()

class csv_upload(FlaskForm):
    file = FileField()
    submit = SubmitField()