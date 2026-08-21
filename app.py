from flask import Flask, render_template, request
from calculator import calc

app = Flask(__name__)

# homepage
@app.route("/")
def acute_care_calc():
    return render_template('index.html') #"Acute Care Calculator"

#tnk calc
@app.route("/tnk-dose-calculator", methods = ["GET", "POST"])
def tnk_calc():
    result = None
    user_weight = None
    unit = None

    if request.method == "POST":
        user_weight = request.form.get("patient_weight")
        unit = request.form.get("weight_unit")

        result = calc(user_weight, unit)        
    
    return render_template("tnk_calculator.html", result = result, weight = user_weight, unit = unit)