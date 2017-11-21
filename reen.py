import sqlite3
conn = sqlite3.connect('reen.sqlite3')
c = conn.cursor()

def decor():
	print("-----------------")

def login():
	while True:
		emal_user = input("email user\n")
		decor()
		c.execute("SELECT email FROM users WHERE email == '%s';" % (emal_user))
		if c.fetchone() == None:
			print("error")
		else:
			name_user = input("name user\n")
			pass_user = input("password user\n")
			decor()
			c.execute("SELECT name,password FROM users WHERE name == '%s' AND password == '%s';" % (name_user, pass_user))
			if c.fetchone() == None:
				print("error")
			else:
				print("loading...")
				return
		

def register():
    new_name_user = input("name new user\n")
    decor()
    new_pass_user = input("password new user\n")
    decor()
    new_emal_user = input("email new user\n")
    if new_emal_user != None and new_name_user and new_pass_user:
    	add_user(new_emal_user, new_name_user, new_pass_user)

def add_user(new_emal_userr, new_name_userr, new_pass_userr):
    c.execute("INSERT INTO users (email, name, password) VALUES ('%s', '%s', '%s')" % (
    	new_emal_userr,
    	new_name_userr, 
    	new_pass_userr))

    conn.commit()

def enter():
	decor()
	ent = input("1. login\n2. registrating\n")
	decor()
	if ent == "1":
		login()
		return
	if ent == "2":
		register()
		return
	else:
		print("error\n")

enter()

c.close()
conn.close()