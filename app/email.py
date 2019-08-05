from flask_mail import Message
from app import application
from app import mail
from flask import render_template
from threading import Thread

# there are 2 contexts
# 1. application context
# 2. request context


def send_async_mail(app, msg):
        # application context to get config realted (eg mailhost, port etc)
    with app.app_context():
        mail.send(msg)


def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body

    Thread(target=send_async_mail, args=(application, msg)).start()


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_email('[Microblog] Reset Your Password',
               application.config['ADMINS'][0],
               recipients=[user.email],
               text_body=render_template(
                   'email/reset_password.txt', user=user, token=token),
               html_body=render_template(
                   'email/reset_password.html', user=user, token=token)
               )
