from flask import Flask, render_template
from db import get_strings
from db import get_drums
from db import get_duhovoi

app = Flask(__name__)

@app.route('/')
def index():

    result = get_strings()

    result1 = get_drums()

    result2 = get_duhovoi()

    return render_template('index.html', title="Xenop", strings=result, drums=result1,duhovoi=result2)

@app.route("/guitar")
def guitar():

    return render_template("guitar.html")

@app.route("/electro-guitar")
def electroguitar():

    return render_template("electro-guitar.html")

@app.route("/balalayka")
def balalayka():

    return render_template("balalayka.html")

@app.route("/bongo")
def bongo():

    return render_template("bongo.html")

@app.route("/drums")
def drums():

    return render_template("drums.html")

@app.route("/triangle")
def triangle():

    return render_template("triangle.html")

@app.route("/saxophone")
def saxophone():

    return render_template("saxophone.html")

@app.route("/clarnet")
def clarnet():

    return render_template("Clarnet.html")

@app.route("/garmoshka")
def garmoshka():

    return render_template("garmoshka.html")

app.run(debug=True)


