
from flask import *
import pymysql
from datetime import datetime, timedelta
app.permanent_session_lifetime=timedelta(minutes=10)
app = Flask(__name__,template_folder="templates",static_folder="static")
app.secret_key="manbigdat"
# Connect to PHPMyAdmin cloud database
connection = pymysql.connect(
    host='sql9.freesqldatabase.com',
    user='sql9601859',
    password='4EmEWs8HSl',
    db='sql9601859'

)

@app.route("/basic")
def index():
    return "<h1>Hello Azure!</h1>"

@app.route('/')
def home():
    return render_template("home.html")









if __name__ == "__main__":
    app.run(debug=True)