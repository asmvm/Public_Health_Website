import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'flask_wtf'])

from wtforms import Form, BooleanField, StringField, PasswordField, validators

class ContactForm(Form):
  first_name = StringField("first-name", [validators.Required()])
  last_name = StringField("last-name", [validators.Required()])
  phone_number = StringField("phone-number")
  email = StringField("email", [validators.Required()])
  subject = StringField("subject", [validators.Required()])
  message = StringField("message", [validators.Required()])
  submit = StringField("send")