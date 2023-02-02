import requests

def get_weather(city_name):
    # First, get the zip code of the city
    response = requests.get(f"http://0.0.0.0:90/city?city_name={city_name}")
    zip_code = int(response.text.split(" ")[-1][:-1])

    # Next, use the zip code to get the weather
    response = requests.get(f"http://0.0.0.0:80/weather?zip_code={zip_code}")
    return response.text

city_name = input("Enter the name of the city: ")
print(get_weather(city_name))

