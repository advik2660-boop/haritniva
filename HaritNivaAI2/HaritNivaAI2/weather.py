import requests

API_KEY = "26910d297c2c155dfdfeb6ab58fa2caf"


def get_weather(location):

    try:

        url = "https://api.openweathermap.org/data/2.5/weather"

        response = requests.get(
            url,
            params={
                "q": location,
                "appid": API_KEY,
                "units": "metric"
            },
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        weather = data["weather"][0]["description"]

        if "rain" in weather.lower():
            advisory = "Rain is expected. Avoid irrigation and postpone pesticide spraying."

        elif temperature >= 35:
            advisory = "High temperature. Irrigate during morning or evening."

        elif wind >= 8:
            advisory = "Strong winds. Avoid spraying pesticides."

        else:
            advisory = "Weather is suitable for normal farming activities."

        return {

            "success": True,

            "temperature": temperature,

            "humidity": humidity,

            "wind": wind,

            "weather": weather.title(),

            "rain": "See Weather Description",

            "sunrise": "-",

            "sunset": "-",

            "advisory": advisory

        }

    except Exception as e:

        import traceback
        traceback.print_exc()

        return {

            "success": False,

            "message": "Unable to fetch weather."

        }