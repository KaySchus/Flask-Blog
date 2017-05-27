from flask import current_app

from flask_mail import Message

from flaskblog.extensions import mail


def send_email(to, subject, template):
	msg = Message(
		subject,
		recipients=[to],
		html=template,
		sender=current_app.config['MAIL_CONFIRMATION_SENDER']
	)

	mail.send(msg)
