import pyrebase
from getpass import getpass

def init():

	firebaseConfig = {
	"apiKey": "AIzaSyA_5aUBBOpw9aimDEhNEBdiMwUEcOWyTqU",
	"authDomain": "henry-molar.firebaseapp.com",
	"databaseURL": "https://henry-molar-default-rtdb.firebaseio.com",
	"projectId": "henry-molar",
	"storageBucket": "henry-molar.appspot.com",
	"messagingSenderId": "151143627901",
	"appId": "1:151143627901:web:ec4629837cb8cc224cc514",
	"measurementId": "G-SLB1JB8KTY"
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



mykey = "a54b0be445cfb7bd35758b6f9bc828e1effdeca854f996a98abe725d"