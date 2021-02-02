import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'flask_wtf'])

from wtforms import  BooleanField, StringField, TextField, IntegerField,   FormField,SelectField, SubmitField, ValidationError, validators
from flask_wtf import FlaskForm, RecaptchaField, CSRFProtect
from wtforms_alchemy import PhoneNumberField
from wtforms.validators import DataRequired, Length, Email
# import phonenumbers
import email_validator

csrf = CSRFProtect()

# class TelephoneForm(FlaskForm):
#     country_code = IntegerField('Country Code', [validators.required()])
#     area_code    = IntegerField('Area Code/Exchange', [validators.required()])
#     number       = StringField('Number')


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
    # phone_number = FormField('Phone Number', TelephoneForm)

    reasons = ["Business: Interested in hiring ..", "Press: Interested in a comment from ..", "Partner: Internested in colloboration project with ..",
              "Careers: Internested in applying to .."]
    def sub_validator(self, field):
      if field.data == -1:
          raise ValidationError('Please select a subject...')

    subject = SelectField(
      u'Subject', choices = reasons, validators=[DataRequired(), sub_validator])

    body = TextField(
        'Message', validators=
        [
            DataRequired(),
            Length(min=4,
            message=('Your message is too short.'))
        ]
    )

    # def validate_phone(self, field):
    #     if len(field) > 16:
    #         raise ValidationError('Invalid phone number.')
    #     try:
    #         input_number = phonenumbers.parse(field.data)
    #         if not (phonenumbers.is_valid_number(input_number)):
    #             raise ValidationError('Invalid phone number.')
    #     except:
    #         input_number = phonenumbers.parse("+1"+field)
    #         if not (phonenumbers.is_valid_number(input_number)):
    #             raise ValidationError('Invalid phone number.')

    # phone = StringField('Phone', validators=[DataRequired(),validate_phone('ContactForm','phone'), Length(min=6, max=40)])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')
    


