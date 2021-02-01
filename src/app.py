from flask import Flask, render_template, request, flash
# Prevent a CSRF attack by making sure that the form submission originates from your web app.
from forms import ContactForm
from flask import Flask
app = Flask(__name__)

app.secret_key = 'development key'
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'donley.gustave@gmail.com'
app.config['MAIL_PASSWORD'] = 'rav3ma5t3r'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  form = ContactForm()

  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      return 'Form posted.'

  elif request.method == 'GET':
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run()