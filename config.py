import os

# application configurations
DEBUG=False
# SQLALCHEMY_DATABASE_URI="postgresql://jea2161:1955@35.227.79.146/proj1part2"
APPNAME=os.getenv('APPNAME', 'homework_helper')
SQLALCHEMY_DATABASE_URI="postgresql://user@127.0.0.1/%s" % APPNAME
SQLALCHEMY_ECHO=False
TESTING=False
HOST='127.0.0.1'
PORT=5432

