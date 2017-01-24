from flask import * 
from models import *
from forms import *

app = Flask(__name__)
user = User()

@app.route('/')
def index():
	return render_template('index.html')


# @app.route('/registration', methods=['POST', 'GET'])
# def register():
# 	fullname = 'Raymond John'
# 	username = 'Ray'
# 	password = 'password'
# 	user.insert_data(fullname=fullname, username=username,password=password)
# 	return "successfully inserted"

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

@app.route('/login', methods=['GET', 'POST'])
def login():
	return 'login page'


