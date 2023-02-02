from flask import Flask, request, redirect

app = Flask(__name__)

zip_code = -1


@app.route('/')
def index():
    return '<h1>Main Page</h1>'


@app.route('/city')
def city_entry():
    city_name = request.args.get('city_name')
    zip_code = find_zip_code(city_name)
    redirect('/result')
    return f"The zip code of the city: {city_name} is {zip_code}."


@app.route('/result')
def result():
    return zip_code


def find_zip_code(city):
    city_to_zip_code = {"Sunnyvale": 94089, "Cupertino": 95014, "San Jose": 95110, "Los Gatos": 95032, "Coyote": 95013}
    return city_to_zip_code[city]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
