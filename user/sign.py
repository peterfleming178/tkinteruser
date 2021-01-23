import tkinter as tk
from firebase import firebase
from tkinter import messagebox
import urllib
import requests
import json

def checkconn():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        return True
    except: 
        return False



auth = firebase.init()

window = tk.Tk()
window.config(bg="white")
window.resizable(False,False)
window.attributes('-topmost', True)
window.title("Sign In")

def reset(arg):
	_email_ = str(email.get())
	if _email_ == "":
		messagebox.showerror("Error","Please enter your email to reset password")
	else:
		if _email_.find("@") != -1 and _email_.find(".") != -1:
			try:
				firebase.reset(auth,_email_)
				messagebox.showinfo("Sent!","The reset link has been sent to your email adress")
			except requests.exceptions.HTTPError as e:
				error_json = e.args[1]
				error = json.loads(error_json)['error']['message']
				messagebox.showerror("Error",error)
			
		else:
			messagebox.showerror("Please enter a valid email")
def _signin_(arg=None):
	_email_ = str(email.get())
	_password_ = str(password.get())
	if _email_ == "" or password == "":
		messagebox.showerror("Error","Please fill all fields")
	else:
		if _email_.find("@") != -1 and _email_.find(".") != -1:
			if checkconn() == False:
				messagebox.showerror("Error","No connection detected please check your internet connection")
			else:
				try:
					firebase.signin(auth=auth,email=str(email.get()),password=str(password.get()))
					window.destroy()
				except:
					messagebox.showerror("Alert","Couldn't sign in check your email and password and please try again")
					
		else:
			messagebox.showerror("Error","Please enter a valid email id")


passw_hide = True

def pass_show_hide(arg):
	global passw_hide
	if passw_hide == True:
		password.config(show="")
		eye.config(text="􀋮")
		passw_hide = False
	elif passw_hide == False:
		password.config(show="*")
		eye.config(text="􀋰")
		passw_hide = True

font = "avenir"


tk.Label(window,text="Email Id:",font=(font,16),fg="black",bg="white").grid(row=1,column=0,pady=20,padx=20)

email = tk.Entry(window,font=(font,16),fg="black",bg="white",insertbackground="black")
email.grid(row=1,column=1,pady=20,padx=20)

tk.Label(window,text="Password:",font=(font,16),fg="black",bg="white").grid(row=2,column=0,pady=0,padx=20)

password = tk.Entry(window,font=(font,16),fg="black",bg="white",show="*",insertbackground="black")
password.grid(row=2,column=1,pady=0,padx=20)

eye = tk.Label(window,fg="grey",bg="white",text="􀋰",font=(font,16))
eye.grid(row=2,column=2,sticky=tk.W)
eye.bind("<Button-1>",pass_show_hide)

reset_ = tk.Label(window,text="forgot passsword? Reset it",bg="white",fg="blue")
reset_.grid(row=3,column=1,pady=(0,20),padx=20)
reset_.bind("<Button-1>",reset)

signin = tk.Button(window,font=(font,16),text="Sign In",command=_signin_)
signin.grid(row=4,column=0,columnspan=2,pady=20)

email.bind("<Return>",lambda event: password.focus)
password.bind("<Return>",_signin_)

window.mainloop()