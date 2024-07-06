import os

UPLOAD_FOLDER = 'uploads/'
DATABASE_CONFIG = {
    'dbname': "postgres",
    'user': "postgres",
    'password': "123",
    'host': "localhost",
    'port': "5432"
}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)