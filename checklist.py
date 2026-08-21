def evaluate_checklist(bleed, dose, time, consent, glucose, labs, nihss, exclusion):
    if bleed == "no":
        return False, "STOP, Do not administer TNK"
    elif dose == "no":
        return False, "STOP, Verify dose before administering"   
    elif time == "no":
        return False, "STOP, Outside standard window" 
    elif consent == "no":
        return False, "STOP, consent required before proceeding"
    elif glucose == "no":
        return False, "STOP, Glucose must be checked"
    elif labs == "no":
        return False, "STOP, Labs required"
    elif nihss == "no":
        return False, "STOP, NIHSS assessment required"
    elif exclusion == "no":
        return False, "STOP, Review exclusion criteria"
    else: # passed all checks
        return True, "ALL CHECKS PASSED, PROCEED TO TNK dosing calculator"