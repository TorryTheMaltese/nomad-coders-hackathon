import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'torry'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/nomad-coders-hackathon'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = basedir + '\\app\\static\\upload_folder'
