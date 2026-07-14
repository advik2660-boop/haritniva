from datetime import datetime, timedelta

from harvest_data import HARVEST_DAYS


def calculate_harvest(crop_name, planting_date):

    planted = datetime.strptime(
        planting_date,
        "%Y-%m-%d"
    )

    harvest_days = HARVEST_DAYS[crop_name]

    harvest_date = planted + timedelta(days=harvest_days)

    today = datetime.today()

    remaining = (harvest_date - today).days

    if remaining < 0:

        stage = "🌾 Ready for Harvest"

    elif remaining < 30:

        stage = "🟡 Nearly Ready"

    else:

        stage = "🌱 Growing"

    confidence = 95

    return {

        "harvest_date":
        harvest_date.strftime("%d %B %Y"),

        "remaining":
        remaining,

        "stage":
        stage,

        "confidence":
        confidence

    }