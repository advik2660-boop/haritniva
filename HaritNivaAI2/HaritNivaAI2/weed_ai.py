from weed_data import WEEDS

def detect_weed(name):

    weed = WEEDS[name]

    if weed["severity"] == "High":
        confidence = 98
    elif weed["severity"] == "Medium":
        confidence = 94
    elif weed["severity"] == "Low":
        confidence = 90
    else:
        confidence = 100

    return {

        "name": name,

        "severity": weed["severity"],

        "control": weed["control"],

        "confidence": confidence

    }