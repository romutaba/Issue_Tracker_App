from flask import *
from flask import Flask
from routes import *

if __name__ == '__main__':
    # app.run(threaded=True,debug=True, use_debugger=False, use_reloader=False)
    app.run(debug=False)
