from flask import Flask

app = Flask(__name__)

@app.route("/")
def acute_care_calc():
    return "<p>Acute Care Calculator</p>"