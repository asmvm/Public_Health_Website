import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'flask_wtf'])
from flask_wtf import FlaskForm
from flask_wtf.file import TextField, TextAreaField, SubmitField, validators

class ContactForm(Form):
  first_name = TextField("first-name", [validators.Required()])
  last_name = TextField("last-name", [validators.Required()])
  phone_number = TextField("phone-number")
  email = TextField("email", [validators.Required()])
  subject = TextField("subject", [validators.Required()])
  message = TextAreaField("message", [validators.Required()])
  submit = SubmitField("send")