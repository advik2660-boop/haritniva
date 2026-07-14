def irrigation_advice(crop, soil, weather, days):

    if weather == "Rain":
        return {
            "status": "No Irrigation",
            "advice": "Rain is expected. Do not irrigate today."
        }

    if soil == "Sandy" and days >= 2:
        return {
            "status": "Irrigate",
            "advice": f"{crop} should be irrigated today."
        }

    if soil == "Loamy" and days >= 4:
        return {
            "status": "Irrigate",
            "advice": f"{crop} should be irrigated today."
        }

    if soil == "Clay" and days >= 6:
        return {
            "status": "Irrigate",
            "advice": f"{crop} should be irrigated today."
        }

    return {
        "status": "Not Required",
        "advice": "Soil moisture is likely sufficient."
    }