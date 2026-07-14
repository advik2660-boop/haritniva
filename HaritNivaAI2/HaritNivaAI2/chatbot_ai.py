import requests

API_KEY = "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"

URL = "https://openrouter.ai/api/v1/chat/completions"


def chatbot_reply(message):

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "tencent/hy3:free",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are HaritNiva AI, an expert AI farming assistant for Indian farmers. "
                    "Answer in a simple, practical way. Help with crops, weather, fertilizers, "
                    "soil, irrigation, pests, diseases, government schemes and sustainable farming."
                )
            },
            {
                "role": "user",
                "content": message
            }
        ]
    }

    try:
        response = requests.post(
            URL,
            headers=headers,
            json=data,
            timeout=30
        )

        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]

        return f"Error: {result}"

    except Exception as e:
        return f"Connection Error: {e}"