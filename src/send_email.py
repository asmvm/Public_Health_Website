# from flask_mail import Mail, Message
# import smtplib

# mail = Mail()

# def sendContactForm(result):
#     msg = Message("Contact Form from Skolo Website",
#                   sender="testing@web-design-johannesburg.com",
#                   recipients=["donley.gustave@gmail.com"])

#     msg.body = """
#     Hello there,
#     You just received a contact form.
#     Name: {}
#     Email: {}
#     Message: {}
#     regards,
#     Webmaster
#     """.format(result['name'], result['email'], result['message'])

#     mail.send(msg)