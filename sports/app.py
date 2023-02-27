from flask import Flask,render_template ,request,redirect

app = Flask(__name__)

SPORTS = ["cricket","vollyball","football"]
registrants = {}

@app.route("/") 
def index():
    return render_template("index.html", sports = SPORTS)


@app.route("/register", methods = ["POST"]) 
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message = name)
    sport = request.form.get("sport")
    if not sport:
        return render_template("error.html", message = sport)
    if sport not in SPORTS:
        return render_template("error.html", message = "Invalid Sports")

    """     
    if not request.form.get("name") or request.form.get("sports") not in SPORTS:
        return render_template("failure.html")
     """
    
    registrants[name]=sport
    return redirect("/registrants")

@app.route("/registrants")
def registrantsfun():
    return render_template("registrants.html", registrants = registrants)

# registrants = registrants here first one is value given to registrants.html and 2nd one is variable in this page
