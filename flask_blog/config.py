import os
class Config():
    SECRET_KEY = '1f02242ffa67ab227f54e9414a69cccc'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    # app.config['MAIL_SENDER'] = os.environ.get('MAIL_SENDER_EMAIL')