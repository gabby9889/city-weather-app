from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Main Page</h1>'


@app.route('/weather')
def weather_entry():
    zip_code = int(request.args.get('zip_code'))
    return f"The weather in the area (Zip Code: {zip_code}) is {find_weather(zip_code)}."


def find_weather(zip_code):
    zip_code_to_weather = {94089: "Sunny", 95014: "Cloudy", 95110: "Windy", 95032: "Rainy", 95013: "Snowy"}
    return zip_code_to_weather[zip_code]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)