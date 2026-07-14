from achievement_ai import get_achievements
from task_ai import add_task, get_tasks
from budget_ai import calculate_budget
print("MARKET_AI LOADED")
from profit_ai import calculate_profit
from disease_ai import detect
from harvest_ai import calculate_harvest
from database import *
from weather import get_weather
from crop_ai import recommend_crops
from flask import Flask, render_template, request, redirect, url_for
from database import *
from chatbot_ai import chatbot_reply
from report_generator import create_report
from flask import send_file
from notification_ai import get_notifications
from weed_ai import detect_weed
from market_ai import get_market

app = Flask(__name__)

create_database()
print("Database created")

@app.route("/")
def home():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    notifications = get_notifications()

    weather_data = get_weather(farmer[4])

    weather_temp = "--"
    weather_desc = "--"
    advisory = "Weather information unavailable."

    if weather_data["success"]:
        weather_temp = weather_data["temperature"]
        weather_desc = weather_data["weather"]
        advisory = weather_data["advisory"]

    tasks = get_tasks()
    nitrogen = farmer[5]
    phosphorus = farmer[6]
    potassium = farmer[7]
    sulfur = farmer[8]
    organic = farmer[9]
    zinc = farmer[10]
    iron = farmer[11]

    soil_health = round(

    ( 
    (nitrogen/300)*100 +
    (phosphorus/60)*100 +
    (potassium/280)*100 +
    (sulfur/20)*100 +
    (organic/1.0)*100 +
    (zinc/1.2)*100 +
    (iron/4.5)*100

    )/7

    )
    return render_template(
        "dashboard.html",

        farmer=farmer,

        notifications=notifications,

        weather_temp=weather_temp,

        weather_desc=weather_desc,

        advisory=advisory,

        tasks=tasks,

        best_crop="Wheat",

        confidence=95,

        soil_health=soil_health,

        nitrogen=nitrogen,
        phosphorus=phosphorus,
        potassium=potassium,
        sulfur=sulfur,
        organic=organic,
        zinc=zinc,
        iron=iron
    )

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        username = request.form["username"]
        contact = request.form["contact"]
        farm = request.form["farm"]
        state = request.form["state"]

        save_farmer(
            name,
            username,
            contact,
            farm,
            state
        )

        return redirect(url_for("home"))

    return render_template("register.html")

@app.route("/weather")
def weather():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    location = farmer[4]

    weather_data = get_weather(location)

    return render_template(
        "weather.html",
        farmer=farmer,
        weather=weather_data
    )

@app.route("/crop", methods=["GET", "POST"])
def crop():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    recommendations = None

    if request.method == "POST":

        soil = request.form["soil"]

        water = request.form["water"]

        seed_budget = int(request.form["seed_budget"])

        fertilizer_budget = int(request.form["fertilizer_budget"])

        labour_budget=int(request.form["labour_budget"])

        land=float(request.form["land"])

        duration = request.form["duration"]

        recommendations = recommend_crops(

            soil,

            water,

            seed_budget,

            fertilizer_budget,

            labour_budget,

            land,

            duration

        )

    return render_template(

        "crop.html",

        farmer=farmer,

        recommendations=recommendations

    )

@app.route("/harvest", methods=["GET","POST"])
def harvest():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    result = None

    if request.method == "POST":

        crop = request.form["crop"]

        planting_date = request.form["planting_date"]

        result = calculate_harvest(
            crop,
            planting_date
        )

    return render_template(
        "harvest.html",
        farmer=farmer,
        result=result
    )

@app.route("/disease", methods=["GET","POST"])
def disease():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    result = None

    if request.method == "POST":

        symptom = request.form["symptom"]

        result = detect(symptom)

    return render_template(
        "disease.html",
        farmer=farmer,
        result=result
    )

@app.route("/profit", methods=["GET","POST"])
def profit():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    result = None

    if request.method == "POST":

        acres = float(request.form["acres"])

        yield_per_acre = float(request.form["yield"])

        selling_price = float(request.form["price"])

        seed = float(request.form["seed"])

        fertilizer = float(request.form["fertilizer"])

        labour = float(request.form["labour"])

        result = calculate_profit(

            acres,

            yield_per_acre,

            selling_price,

            seed,

            fertilizer,

            labour

        )

    return render_template(

        "profit.html",

        farmer=farmer,

        result=result

    )

@app.route("/chatbot", methods=["GET","POST"])
def chatbot():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    answer = None

    if request.method == "POST":

        question = request.form["question"]

        answer = chatbot_reply(question)

    return render_template(
        "chatbot.html",
        farmer=farmer,
        answer=answer
    )

@app.route("/download-report")
def download_report():

    farmer = get_farmer()

    report = {

        "Farmer Name": farmer[0],

        "Farm Name": farmer[3],

        "Location": farmer[4],

        "Generated By": "Vistaar AI",

        "Status": "Farm analysis completed."

    }

    filename = "farm_report.pdf"

    create_report(filename, report)

    return send_file(
        filename,
        as_attachment=True
    )

@app.route("/weed", methods=["GET","POST"])
def weed():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    result = None

    if request.method == "POST":

        weed_name = request.form["weed"]

        result = detect_weed(weed_name)

    return render_template(
        "weed.html",
        farmer=farmer,
        result=result
    )

@app.route("/market", methods=["GET","POST"])
def market():

    print("MARKET ROUTE OPENED")

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    result = None

    if request.method == "POST":

        print("POST RECEIVED")

        crop = request.form["crop"]

        print("Crop =", crop)

        result = get_market(crop, farmer[4])

        print("Result =", result)

        result["crop"] = crop

    return render_template(
        "market.html",
        farmer=farmer,
        result=result
    )

@app.route("/budget", methods=["GET", "POST"])
def budget():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    result = None

    if request.method == "POST":

        seed = float(request.form["seed"])
        fertilizer = float(request.form["fertilizer"])
        labour = float(request.form["labour"])
        other = float(request.form["other"])
        income = float(request.form["income"])

        result = calculate_budget(
            seed,
            fertilizer,
            labour,
            other,
            income
        )

    return render_template(
        "budget.html",
        farmer=farmer,
        result=result
    )

@app.route("/tasks", methods=["GET", "POST"])
def tasks():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    if request.method == "POST":

        task = request.form["task"]
        date = request.form["date"]

        add_task(task, date)

    return render_template(
        "tasks.html",
        farmer=farmer,
        tasks=get_tasks()
    )

@app.route("/achievements")
def achievements():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    return render_template(

        "achievements.html",

        farmer=farmer,

        achievements=get_achievements()

    )

@app.route("/soil")
def soil():

    farmer = get_farmer()

    if farmer is None:
        return redirect(url_for("register"))

    nitrogen = farmer[5]
    phosphorus = farmer[6]
    potassium = farmer[7]
    sulfur = farmer[8]
    organic = farmer[9]
    zinc = farmer[10]
    iron = farmer[11]
    ph = farmer[12]

    soil_health = round(
        (
            (nitrogen / 300) * 100 +
            (phosphorus / 60) * 100 +
            (potassium / 280) * 100 +
            (sulfur / 20) * 100 +
            (organic / 1.0) * 100 +
            (zinc / 1.2) * 100 +
            (iron / 4.5) * 100
        ) / 7
    )

    return render_template(
        "soil.html",
        farmer=farmer,
        soil_health=soil_health,
        nitrogen=nitrogen,
        phosphorus=phosphorus,
        potassium=potassium,
        sulfur=sulfur,
        organic=organic,
        zinc=zinc,
        iron=iron,
        ph=ph
    )

if __name__ == "__main__":
    app.run(debug=True)
