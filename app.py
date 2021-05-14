from  flask import Flask ,redirect,url_for

app = Flask(__name__)

@app.route("/")

def home():
    return "<h1>Welcome to Web application  </h1>"

@app.route("/corona")
def newline():
    return "Let this covid be removed"

@app.route("/<name>")
def name(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("newline"))
if __name__=="__main__":

    app.run(debug=True)