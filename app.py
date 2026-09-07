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

# Post-TNK Care Reference
@app.route("/post-tnk-care")
def post_tnk():
    return render_template("post_tnk.html")
 
# UC Stroke Imaging Selection
@app.route("/stroke-imaging", methods=["GET", "POST"])
def stroke_imaging():
    result = None
 
    if request.method == "POST":
        onset_known = request.form.get("onset_known")
        onset_hours = request.form.get("onset_hours")
        perfusion_deficit = request.form.get("perfusion_deficit")
        awakening = request.form.get("awakening")
        disabling = request.form.get("disabling")
        special_factors = request.form.getlist("special_factors")
        sleep_midpoint = request.form.get("sleep_midpoint")
 
        result = evaluate_imaging(
            onset_known, onset_hours, perfusion_deficit,
            awakening, disabling, special_factors, sleep_midpoint
        )
 
    return render_template("stroke_imaging.html", result=result)
 
# Extended Window IVT Eligibility
@app.route("/extended-window", methods=["GET", "POST"])
def extended_window():
    result = None
 
    if request.method == "POST":
        thrombectomy = request.form.get("thrombectomy")
        hypodensity = request.form.get("hypodensity")
        imaging_type = request.form.get("imaging_type")
        mri_criteria = request.form.get("mri_criteria")
        core = request.form.get("core")
        mismatch_vol = request.form.get("mismatch_vol")
        mismatch_ratio = request.form.get("mismatch_ratio")
 
        result = evaluate_ivt(
            thrombectomy, hypodensity, imaging_type,
            mri_criteria, core, mismatch_vol, mismatch_ratio
        )
 
    return render_template("extended_window.html", result=result)
 
if __name__ == "__main__":
    app.run(debug=True)
