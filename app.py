from flask import Flask, render_template, request
from calculator import calc
from checklist import evaluate_checklist

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

#pre_tnk checklist
@app.route("/pre-tnk-checklist", methods=["GET", "POST"])
def pre_tnk():
    message = None
    passed = False

    if request.method == "POST":
        bleed_answer = request.form.get("neg_bleed")
        dose_answer = request.form.get("verify_dose")
        time_answer = request.form.get("time_confirmed")
        consent_answer = request.form.get("verbal_consent")
        glucose_answer = request.form.get("glucose_results")
        labs_answer = request.form.get("labs_drawn")
        nihss_answer = request.form.get("NIHSS_complete")
        exclusion_answer = request.form.get("reviewed_cleared")

        passed, message = evaluate_checklist(bleed_answer, dose_answer, time_answer, consent_answer, glucose_answer, labs_answer, nihss_answer, exclusion_answer)

    return render_template("pre_tnk.html", message = message, passed = passed)
        