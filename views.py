
from flask import Flask
import sqlite3 as sql
from flask import Flask, redirect, flash, render_template, request, session, abort
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

#session = S

@app.route('/', methods=['POST', 'GET'])
def home():
	if not session.get("logged_in"):
		return render_template('login.html')
	else:
		return render_template('home.html')
   #return ("HI THERE AMIGO")

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.form['password'] == 'password' and request.form['username'] == 'admin':
		session['logged_in'] = True
		username = request.form('username')
		password = request.form('password')
		dbHandler.insertUser(username, password)
		users = sbHandler.retrieveUsers()
		return render_template('result.html')
	else:
		flash('wrong password!')
		return render_template("login.html")

# @app.route('/signin',methods = ['POST', 'GET'])
# def signin():
# 	if request.form['password'] == 'password' and request.form['username'] == 'admin':
# 		session['logged_in'] = True
# 		username = request.form('username')
# 		password = request.form('password')
# 		dbHandler.insertUser(username, password)
# 		users = sbHandler.retrieveUsers()
# 		return render_template('result.html')
# 	else:
# 		flash('wrong password!')
# 		return home()
	

@app.route('/register')
def rgister():
   return render_template('register.html')

#function to add users, clone to add issues.
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
	if request.method == 'POST':
		try:
			fn = request.form['fullname']
			un = request.form['username']
			email = request.form['email']
			password = request.form['password']
			dbHandler.insertUser(fn, un, email, password)
			msg = "Record successfully added"
		except:
			con.rollback()
			msg = "error in insert operation"
		finally:
			return render_template("result.html",msg=msg)
			con.close()


@app.route('/issue')
def issue():
   return render_template("user_enter_issues.html")
   #return "Yes im "


@app.route('/addissue',methods = ['POST', 'GET'])
def addissue():
	if request.method == 'POST':
		try:
			subject = request.form['subject']
			definition = request.form['definition']
			priority = request.form['priority']
			raisedate = request.form['raisedate']
			editdate = request.form['editdate']
			assigned = request.form['assigned']
			closed = request.form['closed']
			dbHandler.insertIssues(subject, definition, priority, raisedate, editdate, assigned, closed)
			msg = "Record successfully added"
		except:
			con.rollback()
			msg = "error in insert operation"
		finally:
			return render_template("result.html",msg = msg)
			con.close()




#lists items in db
@app.route('/list')
def list():
	con = sql.connect("issuetracker.db")
	con.row_factory = sql.Row
	cur = con.cursor()
	cur.execute("select * from users")
	rows = cur.fetchall()
	return render_template("list.html",rows = rows)


#lougout
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('/'))




if __name__ == '__main__':
	app.run(debug=False)