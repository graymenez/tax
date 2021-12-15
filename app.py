from flask import Flask,session,request,render_template,redirect,flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db,connect_db,User
# from forms import RegisterUserForm,LoginUserForm,EditEmail,EditTitle,EditPassword,DeleteAccountForm
from flask_bcrypt import Bcrypt
from datetime import date
from sqlalchemy.exc import IntegrityError
import geocoder
from geopy.geocoders import Nominatim
import requests
import os


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] ='postgresql:///tax_pros_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SQLALCHEMY_ECHO"]=True
app.config['SECRET_KEY']='854f46078d77cb798c4615f5d1bfc1302a28844340fda940b3120671b2c3f26364dd0275e362a9bb952083387599420d6ec9d60fea4791'
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False

debug = DebugToolbarExtension(app)


connect_db(app)

bcrypt = Bcrypt()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin-page')
def admin():
    return render_template('admin.html')

@app.route('/forget-pw')
def forgot_pw():
    return render_template('forgot-password.html')

@app.route('/cards')
def cards():
    return render_template('cards.html')

@app.route('/buttons')
def buttons():
    return render_template('buttons.html')

@app.route('/animations')
def anime():
    return render_template('utilities-animation.html')

@app.route('/sign-up')
def register():
    return render_template('register.html')


@app.route('/secure-payment')
def payments():
    return render_template('payment.html')