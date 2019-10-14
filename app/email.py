from flask import render_template
from app import app


def send_password_reset_email(user):
    token = user.get_reset_password_token()

    send_email('[Microblog] Reset Your Password',
               sender='Admin',
               recipients=[user.email],
               text_body=render_template('email/reset_password.txt',user=user,token=token),
               html_body=render_template('email/reset_password.html',user=user,token=token))
