from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def acute_care_calc():
    return render_template('index.html') #"Acute Care Calculator"

