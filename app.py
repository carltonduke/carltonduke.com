from flask import Flask, render_template, request
import base64

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/cb", methods =["GET", "POST"])
def colorblind():
    if request.method == "POST":
        img64 = request.form.get("img")
        img = base64.b64encode(img64)
        print(img)
    return render_template("cb.html")


#@app.route("/yt")
def colorblind():
    return render_template("yt_dl.html")