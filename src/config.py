import os

UPLOAD_FOLDER = 'uploads/'
DATABASE_CONFIG = {
    'dbname': "your_database",
    'user': "your_user",
    'password': "your_password",
    'host': "your_host",
    'port': "your_port"
}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)