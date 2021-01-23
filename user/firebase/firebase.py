import pyrebase
from getpass import getpass

def init():

	firebaseConfig = {
	"apiKey": "",
	"authDomain": "",
	"databaseURL": "",
	"projectId": "",
	"storageBucket": "",
	"messagingSenderId": "",
	"appId": "",
	"measurementId": ""
	}

	firebase  = pyrebase.initialize_app(firebaseConfig)
	auth = firebase.auth()
	return auth

def signup(auth,email,password):
	user = auth.create_user_with_email_and_password(email,password)
	return user

def signin(auth,email,password):
	user = auth.sign_in_with_email_and_password(email,password)

def reset(auth,email):
	reset = auth.send_password_reset_email(email)

