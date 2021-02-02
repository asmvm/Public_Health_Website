from flask import Flask, render_template, request, flash, redirect, url_for
# Prevent a CSRF attack by making sure that the form submission originates from your web app.
from forms import *
from flask import Flask
from flask_mail import Mail, Message
import smtplib
from flask_wtf import form
import os 
import sys
from config import *

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')





app = Flask(__name__)


app.secret_key = 'development key'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = USER
app.config['MAIL_PASSWORD'] = PASSWORD
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

@app.route('/contact', methods=['POST', 'GET'])
def contact():
    form = ContactForm()
    send_message(request.form)
    # server = smtplib.SMTP('smtp.gmail.com', 465)
    # server.starttls()
    # server.login("donley.gustave@gmail.com", "rav3ma5t3r")
    # server.sendmail("donley.gustave@gmail.com", form.email, form.body)
    # server.quit()
    if form.validate_on_submit():        
        print('-------------------------')
        name = request.form['first_name'] + ' ' + request.form['last_name']
        print(name)
        print(request.form['email'])
        print(request.form['subject'])
        print(request.form['body'])       
        print('-------------------------')
        send_message(request.form)
        # server = smtplib.SMTP('smtp.gmail.com', 465)
        # server.starttls()
        # server.login("donley.gustave@gmail.com", "rav3ma5t3r")
        # server.sendmail("donley.gustave@gmail.com", form.email, form.body)
        # server.quit()
        return redirect('/success')    

    return render_template('contact.html', form=form)

@app.route('/success')
def success():
    return redirect(url_for('contact'), form= form)

def send_message(message):
    print(message.get('name'))

    msg = Message(message.get('subject'), sender = message.get('email'),
            recipients = ['donley.gustave@gmail.com',' alvaro.mcrae@gmail.com', 	'neilrd01@gmail.com'],
            body= message.get('body')
    )  
    mail.send(msg)


# server = smtplib.SMTP('smtp.gmail.com', 465)
# server.starttls()
# server.login("donley.gustave@gmail.com", "rav3ma5t3r")
# server.sendmail("donley.gustave@gmail.com", form.email, form.message)
# server.quit()



# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
# 	form = ContactForm()

    # server = smtplib.SMTP('smtp.gmail.com', 465)
    # server.starttls()
    # server.login("donley.gustave@gmail.com", "rav3ma5t3r")
    # server.sendmail("donley.gustave@gmail.com", form.email, form.message)
    # server.quit()
#   if request.method == 'POST':
#     if form.validate() == False:
#       flash('All fields are required.')
#       return render_template('contact.html', form=form)
#     else:
#       msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
#       msg.body = """
#       From: %s &lt;%s&gt;
#       %s
#       """ % (form.name.data, form.email.data, form.message.data)
#       mail.send(msg)

#       return render_template('contact.html', success=True)

#   elif request.method == 'GET':
#     return render_template('contact.html', form=form)


# @app.route('/contact', methods=['GET', 'POST'])
# def contact():
  # """Standard `contact` form."""
  # form = ContactForm()
  # # if form.validate_on_submit():
  # #     return redirect(url_for("success"))
  # # return render_template(
  # #     "contact.html",
  # #     form=form,
  # #     template="form-template"
  # # )

  # if request.method == 'POST':
  #   if form.validate() == False:
  #     flash('All fields are required.')
  #     return render_template('contact.html', form=form)
  #   else:
  #     msg = Message(form.subject.data, sender= form.email, recipients=['donley.gustave@gmail.com',' alvaro.mcrae@gmail.com', 	'neilrd01@gmail.com'])
  #     msg.body = """
  #     From: %s &lt;%s&gt;
  #     %s
  #     """ % (form.first_name.data + " " + form.last_name.data, form.email.data, form.message.data)
  #     mail.send(msg)

  #     return render_template('contact.html', success=True)

  # elif request.method == 'GET':
  #   return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run()