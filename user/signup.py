import tkinter as tk
from tkinter import messagebox
from .firebase import firebase
import urllib
import requests
import json



def signup():
	auth = firebase.init()

	def checkconn():
		try:
			urllib.request.urlopen('http://216.58.192.142', timeout=1)
			return True
		except: 
			return False
	window = tk.Tk()
	window.config(bg="white")
	window.resizable(False,False)
	window.attributes('-topmost', True)
	window.title("Sign Up")

	font = "avenir"

	def _signup_(arg=None):
		_name_ = str(name.get())
		_email_ = str(email.get())
		_password_ = str(password.get())
		_renterpassword_ = str(renterpassword.get())
		if _name_ != "" and _email_ != "" and _password_ != "" and _renterpassword_ != "":
			if _password_ == _renterpassword_:
				if len(_password_) <= 6:
					messagebox.showerror("Error","Password Length must be more than 6")
				else:
					if _email_.find("@") != -1 and _email_.find(".") != -1:
						if checkconn() == False:
							messagebox.showerror("Error","No connection detected please check your internet connection")
						else:
							try:
								firebase.signup(auth=auth,email=_email_,password=_password_)
								window.destroy()
							except requests.exceptions.HTTPError as e:
								error_json = e.args[1]
								error = json.loads(error_json)['error']['message']
								if error == "EMAIL_EXISTS":
									messagebox.showerror("Error","Email already exists")
								elif error == "INVALID_EMAIL":
									messagebox.showerror("Error","Invalid Email")
								else:
									messagebox.showerror("Error",error)
					else:
						messagebox.showerror("Error","Please enter a valid email id")
			else:
				messagebox.showerror("Error","Passwords do not match, Please Try Again")
		else:
			messagebox.showerror("Error","Please fill all fields")
	global passw_hide
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

	tk.Label(window,text="Name:",font=(font,16),fg="black",bg="white").grid(row=1,column=0,pady=20,padx=20)

	name = tk.Entry(window,fg="black",font=(font,16),bg="white",insertbackground="black")
	name.grid(row=1,column=1,pady=20,padx=20)

	tk.Label(window,text="Email Id:",font=(font,16),fg="black",bg="white").grid(row=2,column=0,pady=20,padx=20)

	email = tk.Entry(window,font=(font,16),fg="black",bg="white",insertbackground="black")
	email.grid(row=2,column=1,pady=20,padx=20)

	tk.Label(window,text="Password:",font=(font,16),fg="black",bg="white").grid(row=3,column=0,pady=20,padx=20)

	password = tk.Entry(window,font=(font,16),fg="black",bg="white",show="*",insertbackground="black")
	password.grid(row=3,column=1,pady=20,padx=20)
	password.bind('<Control-c>', lambda e: 'break')

	eye = tk.Label(window,fg="grey",bg="white",text="􀋰",font=(font,16))
	eye.grid(row=3,column=2,sticky=tk.W)
	eye.bind("<Button-1>",pass_show_hide)

	tk.Label(window,text="Renter Password:",font=(font,16),fg="black",bg="white").grid(row=4,column=0,pady=20,padx=20)

	renterpassword = tk.Entry(window,font=(font,16),bg="white",fg="black",insertbackground="black",show="*")
	renterpassword.grid(row=4,column=1)
	renterpassword.bind('<Control-v>', lambda e: 'break')

	signup = tk.Button(window,font=(font,16),text="Sign Up",command=_signup_,state="disabled")
	signup.grid(row=6,column=0,columnspan=2,pady=20)

	global disabled
	disabled = True
	def enable_disable():
		global disabled
		if disabled == True:
			signup.config(state="normal")
			disabled = False
		elif disabled == False:
			signup.config(state="disabled")
			disabled = True

	check = tk.Checkbutton(window,bg="white",fg="black", text='i agree to the privacy policy', onvalue=1, offvalue=0,command=enable_disable)
	check.grid(row=5,column=0,columnspan=2)
	def setfocus(widget):
		widget.focus_set()

	name.focus_set()
	name.bind("<Return>",lambda event: setfocus(widget=email))
	name.bind("<Down>",lambda event: setfocus(widget=email))

	email.bind("<Up>",lambda event: setfocus(widget=name))
	email.bind("<Return>",lambda event: setfocus(widget=password))
	email.bind("<Down>",lambda event: setfocus(widget=password))

	password.bind("<Up>",lambda event: setfocus(widget=email))
	password.bind("<Return>",lambda event: setfocus(widget=renterpassword))
	password.bind("<Down>",lambda event: setfocus(widget=renterpassword))

	renterpassword.bind("<Up>",lambda event: setfocus(widget=password))
	renterpassword.bind("<Return>",lambda event: setfocus(widget=check))
	renterpassword.bind("<Down>",lambda event: setfocus(widget=check))

	check.bind("<Up>",lambda event: setfocus(renterpassword))
	check.bind("<Return>",lambda event: setfocus(signup))
	check.bind("<Down>",lambda event: setfocus(signup))

	signup.bind("<Up>",lambda event: setfocus(check))
	def signup_(arg=None):
		global disabled
		if disabled == True:
			messagebox.showinfo("Failed","Please agree to the terms to sign up")
		else:
			_signup_()
	signup.bind("<Return>",signup_)

	window.mainloop()

if __name__ == "__main__":
	signup()