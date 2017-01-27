import sqlite3

con = sqlite3.connect('issuetracker.db')
print ("Opened database successfully")

#function to insert user in db
def insertUser(fullname, username, email, password):
	con = sql.connect("issuetracker.db")
	cur = con.cursor
	cur.execute("INSERT INTO users (fullname,username,email,password) VALUES (?,?,?,?)", (fullname,username,email, password))
	users = cur.fetchall() 
	#con.commit()
	con.close()
	return users

#function to retrieve user from db
def retrieveUsers():
	con = sql.connect("issuetracker.db")
	cur = con.cursor
	cur.execute("SELECT username, password FROM users")
	con.commit()
	con.close()

def retrieveIssues():
	con = sql.connect("issuetracker.db")
	cur = con.cursor
	cur.execute("SELECT subject, definition, priority, raise_date, edit_date, is_closed, is_assigned FROM issues_raised")
	con.commit()
	con.close()

def insertIssues(departments, definition, priority, raise_date, edit_date, is_closed, is_assigned):
	con = sql.connect("issuetracker.db")
	cur = con.cursor
	cur.execute("INSERT INTO issues_raised (subject, definition, priority, raise_date, edit_date, is_closed, is_assigned) VALUES (?,?,?,?,?,?,?)", (subject, definition, priority, raise_date, edit_date, is_closed, is_assigned))
	issues = cur.fetchall() #con.commit()
	con.close()
	return issues
