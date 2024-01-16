from flask import Flask, render_template, request, jsonify
import requests
app = Flask(__name__)

# open weather api 
api_key = "2f76294096824872aab19fdfcf466061"
url = "https://api.openweathermap.org/data/2.5/weather"
unit = "metric"

# home page 
@app.route("/")
def home_page():
    return render_template("index.html")

# location 
@app.route("/city", methods=["POST"])
def on_select_city():
    if request.method == "POST":
        city_name = request.form["cityname"]
        global api_key, url, unit
        params = {
            'q':city_name,
            'units': unit,
            'appid': api_key
        }
        data = requests.get(url, params)
        data_json = data.json()
        temperature = int(data_json.get('main', {}).get('temp', 0))

        return render_template("result.html", data=str(temperature))




# run enviornment 
if __name__ == "__main__":
    app.run(debug=True)