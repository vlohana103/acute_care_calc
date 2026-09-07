def evaluate_imaging(onset_known, onset_hours, perfusion_deficit,
                     awakening, disabling, special_factors, sleep_midpoint):
    """
    UC Stroke Imaging Selection Protocol.
    Returns a tuple: (recommendation, reasoning)
    """

    # Unknown onset -> MRI
    if onset_known == "no":
        return ("Order MRI",
                "Unknown onset time — MRI is indicated per UC Stroke Imaging Selection Protocol.")

    # Known onset
    if onset_known == "yes":

        # Stroke on awakening branch
        if awakening == "yes":

            # Disabling and treatable within 4.5hrs of symptom discovery
            if disabling == "yes":
                if special_factors:
                    return ("Order MRI",
                            "Stroke on awakening, disabling, treatable within 4.5hrs, with special factors "
                            f"({', '.join(special_factors)}) present — MRI indicated.")
                else:
                    return ("Order MRI",
                            "Stroke on awakening, disabling, and treatable within 4.5hrs of symptom discovery — MRI indicated.")

            # Not disabling within 4.5hrs — check sleep midpoint window
            if sleep_midpoint == "yes":
                if perfusion_deficit == "yes":
                    return ("Order CTP",
                            "Stroke on awakening, treatable within 9hrs of sleep midpoint, with reasonable likelihood "
                            "of perfusion deficit (DMVO or NIHSS ≥4 with cortical signs) — CTP indicated.")
                else:
                    return ("Not a candidate for Extended Window IVT",
                            "Stroke on awakening, within 9hrs of sleep midpoint, but no reasonable likelihood "
                            "of perfusion deficit — treat per standard protocol.")
            else:
                return ("Outside treatment window",
                        "Stroke on awakening but outside 9hrs of sleep midpoint — treat per standard protocol.")

        # Not a stroke on awakening — check known onset timing
        if onset_hours == "extended":
            # Known onset >4.5hrs and <=9hrs
            if perfusion_deficit == "yes":
                return ("Order CTP",
                        "Known onset >4.5hrs and ≤9hrs with reasonable likelihood of perfusion deficit "
                        "(DMVO or NIHSS ≥4 with cortical signs) — CTP indicated.")
            else:
                return ("Not a candidate for Extended Window IVT",
                        "Known onset >4.5hrs and ≤9hrs but no reasonable likelihood of perfusion deficit — "
                        "treat per standard protocol.")

        # Within standard 4.5hr window
        if onset_hours == "standard":
            return ("Within standard 4.5hr window",
                    "Known onset ≤4.5hrs — treat per standard protocol. Extended window imaging not required.")

    return ("Unable to determine",
            "Insufficient information provided. Please review inputs and try again.")