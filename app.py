
from flask import *
import pymysql
from datetime import datetime, timedelta
app.permanent_session_lifetime=timedelta(minutes=10)
app = Flask(__name__,template_folder="templates",static_folder="static")
app.secret_key="manbigdat"
# Connect to PHPMyAdmin cloud database
db = pymysql.connect(
    host='sql9.freesqldatabase.com',
    user='sql9601859',
    password='4EmEWs8HSl',
    db='sql9601859'

)
@app.route("/first", methods=["GET", "POST"])
def first():
    if request.method == "POST":
        # Retrieve form data
        min_lat = request.form["min_lat"]
        max_lat = request.form["max_lat"]
        min_population = request.form["min_population"]
        max_population = request.form["max_population"]

        # Construct SQL query
        query = "SELECT city, State, Population, lat, lon FROM city WHERE lat BETWEEN %s AND %s AND Population BETWEEN %s AND %s"
        params = (min_lat, max_lat, min_population, max_population)

        # Execute SQL query
        cursor = db.cursor()
        cursor.execute(query, params)

        # Fetch results
        results = cursor.fetchall()
        print(results)

        # Render template with results
        return render_template("first.html", results=results)

    # Render the search form
    return render_template("allquestions.html")


@app.route("/bonus", methods=["GET", "POST"])
def bonus():
    if request.method == "POST":
        # Retrieve form data
        state_name = request.form.get("state_name")
        min_population = request.form["min_population2"]
        max_population = request.form["max_population2"]

        # Construct SQL query
        query = "SELECT city, state, population, lat, lon FROM city WHERE state = %s AND population BETWEEN %s AND %s"
        params = (state_name, min_population, max_population)

        # Execute SQL query
        cursor = db.cursor()
        cursor.execute(query, params)

        # Fetch results
        results = cursor.fetchall()

        # Render template with results
        return render_template("first.html", results=results)

    # Render the search form
    return render_template("allquestions.html")







@app.route("/basic")
def index():
    return "<h1>Hello Azure!</h1>"

@app.route('/')
def home():
    return render_template("home.html")









if __name__ == "__main__":
    app.run(debug=True)
