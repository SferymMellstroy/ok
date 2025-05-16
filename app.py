from flask import Flask, render_template
from db import get_strings
from db import get_drums
from db import get_duhovoi
from flask import request
from db import add_user
from db import get_top_strings
from db import get_top_drums
from db import get_top_duhovoi

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
     
    strings = get_top_strings()

    return render_template("guitar.html", ste = strings)


@app.route("/electro-guitar")
def electroguitar():

    strings = get_top_strings()

    return render_template("electro-guitar.html", ste = strings)

@app.route("/balalayka")
def balalayka():

    strings = get_top_strings()

    return render_template("balalayka.html", ste = strings)

@app.route("/bongo")
def bongo():

    drums = get_top_drums()

    return render_template("bongo.html", dru = drums)

@app.route("/drums")
def drums():

    drums = get_top_drums()

    return render_template("drums.html", dru = drums)

@app.route("/triangle")
def triangle():

    drums = get_top_drums()

    return render_template("triangle.html", dru = drums)

@app.route("/saxophone")
def saxophone():

    duhovoi = get_top_duhovoi()

    return render_template("saxophone.html", duh = duhovoi)

@app.route("/clarnet")
def clarnet():

    duhovoi = get_top_duhovoi()

    return render_template("clarnet.html", duh = duhovoi)

@app.route("/garmoshka")
def garmoshka():

    duhovoi = get_top_duhovoi()

    return render_template("garmoshka.html", duh = duhovoi)


@app.route("/about")
def about():

    return render_template("about.html")


app.run(debug=True)


