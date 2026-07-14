from datetime import datetime


def get_notifications():

    month = datetime.now().month

    notifications = []

    if month in [6, 7, 8]:

        notifications.append("🌧 Monsoon season: Check field drainage.")

    if month in [10, 11]:

        notifications.append("🌱 Good time for wheat sowing.")

    if month in [3, 4]:

        notifications.append("🌾 Harvest season for many rabi crops.")

    notifications.append("💧 Check soil moisture before irrigation.")

    notifications.append("🧪 Monitor fertilizer application schedule.")

    return notifications