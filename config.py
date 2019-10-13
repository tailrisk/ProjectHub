# Config file to enforce seperation of concerns
# WTForms - for validating inputs
# SQlAlchemy - for handling database connections
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flaskdemo:flaskdemo@flaskdemo.cwsaehb7ywmi.us-east-1.rds.amazonaws.com:3306/flaskdemo'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'projects.sqlite'

#SQLALCHEMY_POOL_RECYCLE = 3600

#WTF_CSRF_ENABLED = True
#SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
