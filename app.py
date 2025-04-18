from flask import Flask, render_template
from db import get_strings

app = Flask(__name__)

@app.route('/')
def index():
    #вызвать 

    return render_template('index.html', title="Xenop", strings=[])



app.run(debug=True)

