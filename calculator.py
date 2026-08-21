
def calc(weight_num:float, weight_unit:str):
    # enter_weight = input("Enter the Patient's weight:\n")
    # weight_unit = input("is the Weight in kgs or lbs?\n")
    reminder = "Draw up in 5mL syrgine\nAdminister IV push over 5 seconds\nFlush IV line with 10 mL Normal Saline before and after"

    weight_num = float(weight_num) # converts from html string to float

    # Checks to see if lbs or kg
    if weight_unit == "lbs":
        weight_num /= 2.205 # converts to kg
    else: 
        weight_num  # keeps kg


    # Calculates Dose and Volume
    if weight_num >= 98:
        return f"{reminder}<br><br>Dose: 25 mg<br>Volume: 5 ml"

    elif weight_num >= 94:
        return f"{reminder}<br><br>Dose: 24 mg<br>Volume: 4.8 ml"

    elif weight_num >= 90:
        return f"{reminder}<br><br>Dose: 23 mg<br>Volume: 4.6 ml"

    elif weight_num >= 86:
        return f"{reminder}<br><br>Dose: 22 mg<br>Volume: 4.4 ml"

    elif weight_num >= 82:
        return f"{reminder}<br><br>Dose: 21 mg<br>Volume: 4.2 ml"

    elif weight_num >= 78:
        return f"{reminder}<br><br>Dose: 20 mg<br>Volume: 4 ml"

    elif weight_num >= 74:
        return f"{reminder}<br><br>Dose: 19 mg<br>Volume: 3.8 ml"

    elif weight_num >= 70:
        return f"{reminder}<br><br>Dose: 18 mg<br>Volume: 3.6 ml"

    elif weight_num >= 66:
        return f"{reminder}<br><br>Dose: 17 mg<br>Volume: 3.4 ml"

    elif weight_num >= 62:
        return f"{reminder}<br><br>Dose: 16 mg<br>Volume: 3.2 ml"

    elif weight_num >= 58:
        return f"{reminder}<br><br>Dose: 15 mg<br>Volume: 3 ml"

    elif weight_num >= 54:
        return f"{reminder}<br><br>Dose: 14 mg<br>Volume: 2.8 ml"

    elif weight_num >= 50:
        return f"{reminder}<br><br>Dose: 13 mg<br>Volume: 2.6 ml"

    elif weight_num >= 46:
        return f"{reminder}<br><br>Dose: 12 mg<br>Volume: 2.4 ml"

    elif weight_num >= 42:
        return f"{reminder}<br><br>Dose: 11 mg<br>Volume: 2.2 ml"

    elif weight_num >= 40:
        return f"{reminder}<br><br>Dose: 10 mg<br>Volume: 2 ml"

    elif weight_num <= 40:    
        return f"{reminder}<br><br>Consult Pharmcist!"
    else:
        return "invalid input"