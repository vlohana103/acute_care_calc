# Acute Care Calculator
 
A Flask-based web application providing clinical reference tools for acute ischemic stroke management, based on UC Stroke Team protocols. Built as an educational and board exam study aid.
 
> ⚠️ **Educational Use Only.** This tool is intended for board exam preparation and clinical reference study. It is not a substitute for clinical judgment, institutional protocols, or physician oversight.
 
---
 
## Features
 
| Tool | Description |
|------|-------------|
| **Pre-TNK Checklist** | 8-point safety checklist before TNK administration |
| **TNK Dose Calculator** | Weight-based tenecteplase dosing (0.25 mg/kg, max 25mg) with kg/lbs conversion |
| **Post-TNK Care Reference** | Monitoring schedule and warning signs after administration |
| **Stroke Imaging Selection** | MRI vs CTP decision tool based on UC Stroke Imaging Selection Protocol |
| **Extended Window IVT Eligibility** | Eligibility checker for 4.5–24hr treatment window via MRI or CTP pathway |
 
---
 
## Tech Stack
 
- **Backend:** Python 3, Flask
- **Frontend:** HTML, CSS (no JavaScript frameworks)
- **Templating:** Jinja2
- **Architecture:** Modular — logic separated into individual Python modules per tool
---
 
## Project Structure
 
```
acute_care_calc/
├── app.py               # Flask routes
├── calculator.py        # TNK dose calculation logic
├── checklist.py         # Pre-TNK safety checklist logic
├── imaging.py           # UC Stroke Imaging Selection logic
├── ivt.py               # Extended Window IVT eligibility logic
├── requirements.txt
├── .gitignore
└── templates/
    ├── base.html        # Shared layout
    ├── index.html       # Homepage
    ├── pre_tnk.html     # Pre-TNK Checklist
    ├── tnk_calculator.html
    ├── post_tnk.html
    ├── stroke_imaging.html
    └── extended_window.html
```
 
---
 
## Setup & Installation
 
```bash
# Clone the repo
git clone https://github.com/vlohana103/acute_care_calc.git
cd acute_care_calc
 
# Create and activate virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
 
# Install dependencies
pip install -r requirements.txt
 
# Run the app
python app.py
```
 
Visit `http://127.0.0.1:5000` in your browser.

---
 
## Development Notes
 
This project was built as a learning exercise in Python web development using Flask. AI-assisted development tools were used during the Flask/HTML/Jinja2 implementation phases, with all outputs reviewed and validated against the source protocol materials.
 
---

## Protocol Sources
 
- Stroke Imaging Selection Protocol (UC Stroke Team)
- Stroke Extended Window IVT Protocol (UC Stroke Team)
- Tenecteplase Dosing Reference Card — Acute Ischemic Stroke (0.25 mg/kg, max 25mg)
