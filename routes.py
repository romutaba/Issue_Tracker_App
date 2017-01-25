from flask import * 
from models import *
from forms import *
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
user = User()

# @app.route('/registration', methods=['POST', 'GET'])
# def register():
#   fullname = 'Raymond John'
#   username = 'Ray'
#   password = 'password'
#   user.insert_data(fullname=fullname, username=username,password=password)
#   return "successfully inserted"


#user sign up form using wtforms 
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


#user login form using wtforms 
# @app.route('/index', methods=['GET', 'POST'])
# def login():
#     return 'login page'


@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #drop the session
        session.pop('user', None)
        if request.form['password'] == 'password':
            session['user'] = request.form['username']
            #create the landing page
            return redirect(url_for('homepage'))

    return render_template('index.html')


@app.route('/homepage')
def homepage():
    #ensure user has session
    if g.user:
        return render_template('homepage.html')

    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']




