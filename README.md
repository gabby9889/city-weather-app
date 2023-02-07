# city-weather-app
### Introduction
The City-Zipcode-Weather App is a system that allows users to find the weather of a city by entering the city name. The system consists of two microservices, one to get the zip code of the city and another to get the weather of the area based on the zip code.  
### Clone the repository
```bash
git clone git@github.com:gabby9889/city-weather-app.git
```

### Zipcode APP
Build the image:
```bash 
docker build -t zipcodeimage .
```
<img width="970" alt="Screen Shot 2023-02-01 at 10 28 57 PM" src="https://user-images.githubusercontent.com/116316971/216248687-c8ee17df-fa1d-419e-a13f-f7b6227e69c5.png">

Run the container:
```bash 
docker run -d -p 90:80 zipcodeimage
```
<img width="969" alt="Screen Shot 2023-02-01 at 10 30 08 PM" src="https://user-images.githubusercontent.com/116316971/216248860-5b781352-54b5-472c-bab9-5cee45def60f.png">

For Client:
<img width="473" alt="Screen Shot 2023-02-01 at 10 30 48 PM" src="https://user-images.githubusercontent.com/116316971/216248977-a647eb5d-499d-4c6e-97db-60568c3111e3.png">

### Weather APP
Build the image:
```bash 
docker build -t weatherimage .
```
<img width="991" alt="Screen Shot 2023-02-01 at 10 31 46 PM" src="https://user-images.githubusercontent.com/116316971/216249145-c6aaccdc-0b78-4cd4-80ac-58ca9086f199.png">

Run the container:
```bash 
docker run -d -p 80:80 weatherimage
```
<img width="1006" alt="Screen Shot 2023-02-01 at 10 32 30 PM" src="https://user-images.githubusercontent.com/116316971/216249281-2434ee0a-5716-4e5a-b7e3-8b8eec4ac316.png">

For Client:
<img width="428" alt="Screen Shot 2023-02-01 at 10 32 57 PM" src="https://user-images.githubusercontent.com/116316971/216249351-e82013de-a767-4801-b405-ea867bf5e19c.png">

### Make two microservices work together
'user.py' uses the requests library to make HTTP requests to the two microservices. The get_weather function first makes a request to the second microservice (the one that returns the zip code for a given city) and extracts the zip code from the response. It then makes a request to the first microservice (the one that returns the weather for a given zip code) and returns the weather information.

The code takes the city name as input from the user and calls the get_weather function to get the weather information.

<img width="892" alt="Screen Shot 2023-02-01 at 10 35 58 PM" src="https://user-images.githubusercontent.com/116316971/216249889-1944570b-19e1-4cb9-8678-4d76b22beff9.png">


