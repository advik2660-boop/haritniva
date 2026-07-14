print("NEW CROP_AI LOADED")
from crop_data import CROPS

print(CROPS)
print(CROPS[0])
print(CROPS[0].keys())

def recommend_crops(

    soil,

    water,

    seed_budget,

    fertilizer_budget,

    labour_budget,

    land,

    duration

):

    results=[]

    for crop in CROPS:

        score=0

        if soil in crop["soil"]:
            score+=30

        if water==crop["water"]:
            score+=25

        if seed_budget>=crop["seed_cost"]:
            score+=10

        if fertilizer_budget>=crop["fertilizer_cost"]:
            score+=10

        if labour_budget>=crop["labour_cost"]:
            score+=10

        if duration==crop["duration"]:
            score+=15

        confidence=score

        gross_income=crop["profit_per_acre"]*land

        seed_total=crop["seed_cost"]*land

        fertilizer_total=crop["fertilizer_cost"]*land

        labour_total=crop["labour_cost"]*land

        net_profit=(
            gross_income
            -seed_total
            -fertilizer_total
            -labour_total
        )

        results.append({

            "name":crop["name"],

            "confidence":confidence,

            "gross_income":gross_income,

            "net_profit":net_profit,

            "seed_total":seed_total,

            "fertilizer_total":fertilizer_total,

            "labour_total":labour_total,

            "duration":crop["duration"],

            "water":crop["water"]

        })

    results.sort(

        key=lambda x:(

            x["confidence"],

            x["net_profit"]

        ),

        reverse=True

    )

    return results[:3]