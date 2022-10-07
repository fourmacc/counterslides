#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from enum import unique
import time
import json
from turtle import up
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
from flask_wtf import Form
import datetime
import socket
import sys
import serial 

# Configuration Keys

SQLALCHEMY_TRACK_MODIFICATIONS = False

app = Flask(__name__)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)
migrate = Migrate(app,db)






# connect to a local postgresql database
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Newreign34:Localhost:5432/subscribers'

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Newsignings(db.Model):
    __tablename__ = 'newsignings'

    phone = db.Column(db.Integer, unique = True, primary_key=True)
    email = db.Column(db.String(50), nullable = False)
    region_id = db.Column(db.Integer, nullable = True)

    def __repr__(self, phone, email, region_id):
      self.phone = phone
      self.email = email
      self.region_id = region_id

class Temphumid(db.Model):
    __tablename__='temphumid'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float, nullable=True)
    humidity = db.Column(db.Float, nullable=True)
    time = db.Column(db.DateTime, nullable = False)

    def __repr__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity  

# arduinoData=serial.Serial('com5',9600)
# time.sleep(2)
# while True:
#     while(arduinoData.inWaiting()==0):
#         pass
#     dataPacket=arduinoData.readline()
#     dataPacket=str(dataPacket, 'utf-8')
#     dataPacket=dataPacket.strip('\r\n')
#     dataPacket=arduinoData.readline()
#     potVal=dataPacket
#     # vol=(5./1023. * (potVal-17.))
#     # vol=round(vol,1)
#     print(dataPacket)

# class Test(db.Model):
#     __tablename__='test'
#     id=db.Column(db.Float(arduinoData), primary_key=True)
    

         
#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime



#----------------------------------------------------------------------------#
# Controllers.
#----------------------------------------------------------------------------#
@app.route('/')
def index():
    return render_template('forms/new_sub.html')






@app.route('/newsignings/sign_up', methods = ['POST'])
def sign_up():
    phone = request.form.get('phone')
    email = request.form.get('email')
    newsigns = Newsignings(phone = phone,email = email)
    db.session.add(newsigns)
    db.session.commit()
    return render_template('pages/confirm.html')
    







































    # Default port:
if __name__ == '__main__':
    app.run()
