from flask import Flask,render_template ,request

app = Flask(__name__)

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/personal", methods= ["POST"]) # by default method = 'get'
def personal():
    return render_template("personal.html",name = request.form.get("name","Admin Balbir Singh"))

# request.args.get()  # from url or GET
# request.for,.get() # from post (security)


""" 
@app.route("/", methods = ["GET","POST"]) 
def index():
    if request.methods =="GET":
        return render_template("index.html")
    if request.methods == "POST":
        return render_template("personal.html",name = request.form.get("name","Admin Balbir Singh"))
 """
if __name__ =='__main__':
    app.run()