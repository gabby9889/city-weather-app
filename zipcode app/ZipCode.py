from flask import Flask, request
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Main Page</h1>'


@app.route('/city')
def city_entry():
    city_name = request.args.get('city_name')
    zip_code = find_zip_code(city_name)
    weather_response = requests.get(f"http://weatherapp:120/weather?zip_code={zip_code}").text
    weather = weather_response.split()[-1][:-1]
    return f"The zip code of the city: {city_name} is {zip_code}. The weather in the area is: {weather}."


def find_zip_code(city):
    city_to_zip_code = {"Sunnyvale": 94089, "Cupertino": 95014, "San Jose": 95110, "Los Gatos": 95032, "Coyote": 95013}
    return city_to_zip_code[city]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)