def evaluate_ivt(thrombectomy, hypodensity, imaging_type,
                 mri_criteria, core, mismatch_vol, mismatch_ratio):
    """
    Extended Window IVT Eligibility Protocol.
    Returns a tuple: (eligible: bool, message: str)
    Recommendations are for patients who:
    1. Are NOT planned for thrombectomy treatment
    2. Do NOT have subacute-appearing hypodensity on CTH
    """

    # Exclusion 1 — planned for thrombectomy
    if thrombectomy == "yes":
        return (False,
                "NOT ELIGIBLE: Patient is planned for thrombectomy treatment. "
                "Extended Window IVT is not indicated — proceed with thrombectomy plan.")

    # Exclusion 2 — subacute hypodensity on CTH
    if hypodensity == "yes":
        return (False,
                "NOT ELIGIBLE: Subacute-appearing hypodensity present on CTH. "
                "Extended Window IVT is contraindicated.")

    # MRI pathway
    if imaging_type == "mri":
        if mri_criteria == "yes":
            return (True,
                    "ELIGIBLE for Extended Window IVT via MRI pathway: Evidence of acute diffusion "
                    "restriction WITHOUT corresponding FLAIR signal on WAKE-UP protocol MRI confirmed.")
        else:
            return (False,
                    "NOT ELIGIBLE via MRI pathway: Diffusion restriction without corresponding FLAIR signal "
                    "on WAKE-UP MRI not confirmed.")

    # CTP pathway — ALL THREE criteria must be met
    if imaging_type == "ctp":
        try:
            core_val = float(core)
            mismatch_vol_val = float(mismatch_vol)
            mismatch_ratio_val = float(mismatch_ratio)
        except (TypeError, ValueError):
            return (False, "Invalid CTP values entered. Please enter numeric values for all CTP criteria.")

        if core_val >= 70:
            return (False,
                    f"NOT ELIGIBLE: Predicted core volume is {core_val}cc — must be <70cc for eligibility.")

        if mismatch_vol_val < 20:
            return (False,
                    f"NOT ELIGIBLE: Mismatch volume is {mismatch_vol_val} — must be ≥20 for eligibility.")

        if mismatch_ratio_val < 1.2:
            return (False,
                    f"NOT ELIGIBLE: Mismatch ratio is {mismatch_ratio_val} — must be ≥1.2 for eligibility.")

        return (True,
                f"ELIGIBLE for Extended Window IVT via CTP pathway: All three criteria met — "
                f"Core {core_val}cc (<70cc ✓), Mismatch volume {mismatch_vol_val} (≥20 ✓), "
                f"Mismatch ratio {mismatch_ratio_val} (≥1.2 ✓).")

    return (False, "Please select an imaging type (MRI or CTP) to determine eligibility.")