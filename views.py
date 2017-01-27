
from flask import Flask
import sqlite3 as sql
from flask import Flask, redirect, flash, render_template, request, session, abort, url_for
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)




@app.route('/', methods=['POST', 'GET'])
def home():
	if not session.get("logged_in"):
		return render_template('login.html')
	else:
		return render_template('home.html')
   #return ("HI THERE AMIGO")

@app.route('/login', methods=['POST', 'GET'])
def login():
	if request.method == 'POST':
		session['logged_in'] = True
		Username = request.form.get('username')
		Password = request.form.get('password')
		con = sql.connect("issuetracker.db")
		con.row_factory = sql.Row
		cur = con.cursor()
		result= cur.execute("SELECT username, password FROM users where username=?",[Username])
		result.fetchone()
		if result is not None:
			#print("halooooooo")
			return render_template("home.html")

		else:
			print('Try again')
		#return render_template('result.html')
	else:
		flash('wrong password!')
		return render_template("login.html")
		con.close()
	

@app.route('/register')
def register():
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
			with sql.connect("issuetracker.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO users (fullname,username,email, password) VALUES (?,?,?,?)", (fn,un,email,password))
				con.commit()
				msg = "Record successfully added"
		except:
			con.rollback()
			msg = "error in insert operation"
		finally:
			return render_template("result.html",msg=msg)
			con.close()


@app.route('/issue')
def issue():

	if not session.get("logged_in"):
		return render_template('login.html')
	else:
		return render_template("user_enter_issues.html")
   #return "Yes im "


@app.route('/addissue',methods = ['POST', 'GET'])
def addissue():
	if request.method == 'POST':
		try:
			departments = request.form['departments']
			definition = request.form['definition']
			priority = request.form['priority']
			raisedate = request.form['raisedate']
			editdate = request.form['editdate']
			assigned = request.form['assigned']
			closed = request.form['closed']

			with sql.connect("issuetracker.db") as con:
				cur = con.cursor()
				cur.execute("INSERT INTO issues_raised (subject, definition, priority, raise_date, edit_date) VALUES (?,?,?,?,?)", (departments, definition, priority, raisedate, editdate))
				con.commit()
				msg = "Record successfully added"
			
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
    session.pop('users', None)
    return redirect(url_for('login'))

@app.route('/getSession')
def getsession():
    '''
    getSessions
    '''
    if 'userz' in session:
        return session['userz']
    return "Not logged in !"




if __name__ == '__main__':
	app.run(debug=False)