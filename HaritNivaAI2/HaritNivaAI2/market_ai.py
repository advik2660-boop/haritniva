
import requests

API_KEY = "579b464db66ec23bdd0000015e233d33d8bd4ea345f8268208bd124f"

def get_market(crop, location):
    url = (
    "https://api.data.gov.in/resource/"
    "9ef84268-d588-465a-a308-a864a43d0070"
    f"?api-key={API_KEY}"
    "&format=json"
    f"&filters[commodity]={crop}"
    "&limit=10000"
)
    try:

        response = requests.get(
    url,
    timeout=30,
    headers={
        "User-Agent": "Mozilla/5.0"
    }
)
        data = response.json()

        print("Available crops:")

        crops = set()

        for record in data["records"]:
           crops.add(record["commodity"])

        print(sorted(crops))

        print("TOTAL RECORDS RETURNED:", len(data["records"]))

        for record in data["records"][:20]:
           print(record["commodity"])
        for record in data["records"]:

           # First preference: same crop + same location
           for record in data["records"]:
            if (
                record["commodity"].lower() == crop.lower()
                and (
                     location.lower() in record["state"].lower()
                     or location.lower() in record["district"].lower()
                    )
        ):
                  return {
                          "crop": crop,
                          "price": float(record["modal_price"]) / 100,
                          "unit": "kg",
                          "market": record["market"],
                          "state": record["state"],
                          "date": record["arrival_date"],
                          "trend": "Live",
                          "advice": f"Live price from {record['market']}, {record['state']}."
                  }

        # If not found in that location, show any market in India
        for record in data["records"]:
           if record["commodity"].lower() == crop.lower():
                return {
                        "crop": crop,
                        "price": float(record["modal_price"]) / 100,
                        "unit": "kg",
                        "market": record["market"],
                        "state": record["state"],
                        "date": record["arrival_date"],
                        "trend": "Live",
                        "advice": f"Price from {record['market']}, {record['state']} (nearest available record)."
                       }

                return {

                    "crop": crop,

                    "price": float(record["modal_price"]) / 100,

                    "unit": "kg",

                    "market": record["market"],

                    "state": record["state"],

                    "date": record["arrival_date"],

                    "trend": "Live",

                    "advice": "Live Government Market Price"

                }

    except Exception as e:

        print(e)

    return {

        "crop": crop,

        "price": "N/A",

        "unit": "kg",

        "market": "-",

        "state": "-",

        "date": "-",

        "trend": "Unavailable",

        "advice": "Commodity not found"

    }

   