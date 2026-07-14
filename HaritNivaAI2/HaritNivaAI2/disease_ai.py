from disease_data import DISEASES

def detect(symptom):

    info = DISEASES[symptom]

    confidence = 95

    return {

        "symptom": symptom,

        "disease": info["disease"],

        "solution": info["solution"],

        "confidence": confidence

    }