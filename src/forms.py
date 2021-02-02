import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'flask_wtf'])

from wtforms import  BooleanField, StringField, TextField, SubmitField, validators
from flask_wtf import FlaskForm, RecaptchaField, CSRFProtect
from wtforms.validators import DataRequired, Length, Email
import email_validator

csrf = CSRFProtect()


class ContactForm(FlaskForm):
    """Contact form."""
    first_name = StringField(
        'First Name', validators=
        [DataRequired()]
    )
    last_name = StringField(
        'Last Name', validators=
        [DataRequired()]
    )
    email = StringField(
        'Email', validators=
        [
            Email(message=('Not a valid email address.')),
            DataRequired()
        ]
    )
    subject = StringField(
        'Subject', validators=
        [DataRequired()]
    )
    body = TextField(
        'Message', validators=
        [
            DataRequired(),
            Length(min=4,
            message=('Your message is too short.'))
        ]
    )

    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


