from flask import Flask, render_template
from db import get_strings
from db import get_drums
from db import get_duhovoi
from flask import request
from db import add_user

app = Flask(__name__)

@app.route('/')
def index():

    result = get_strings()

    result1 = get_drums()

    result2 = get_duhovoi()

    return render_template('index.html', title="Xenop", strings=result, drums=result1,duhovoi=result2)


@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        print(f"Username: {username}, Email: {email}, Password: {password}")
        add_user(username, email, password)
    return render_template("sign_up.html", title = "Registration form")

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


@app.route("/about")
def about():

    return render_template("about.html")

app.run(debug=True)


