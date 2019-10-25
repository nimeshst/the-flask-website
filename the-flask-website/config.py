import os
import yaml

db = yaml.load(open('db.yaml'))
MYSQL_HOST = db['mysql_host']
MYSQL_USER = db['mysql_user']
MYSQL_PASSWORD =db['mysql_password']
MYSQL_DB = db['mysql_db']

class Config(object):
    # declare configiration variables here variables 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'astalavista'

    # database configiration
    # mysql://scott:tiger@localhost/mydatabase
    SQLALCHEMY_DATABASE_URI ="mysql+pymysql://"+MYSQL_USER+":"+MYSQL_PASSWORD+"@"+MYSQL_HOST+"/"+MYSQL_DB
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True    
