#Import required module

import requests

#Use Openweathermap website to get the api_key of your own
#Implement it in a variable or your choice

API_KEY = "GET the API key from the website"

#Get the URL of that website

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

#Fetch Two functions

def get_weather(city):
     params = {
          "q":city,
          "appid":API_KEY,
          "units":"metric"
     }

     #Use GET requests to get data from URL
     response = requests.get(BASE_URL, params=params)

     #Call the requests to a json
     return response.json()

def display_weather(weather_data):
     if weather_data.get("cod") != 200:
          print(f"Error: {weather_data.get('message', 'No data Found')}")
     else:
          #Instead of putting it inside the PRINT statement, Call Multiple Variables to a json data.
          main = weather_data['main']
          wind = weather_data['wind']
          weather = weather_data['weather']

          print(f"City: {weather_data['name']}") #OR without the variables
                                                  #print(f"City: ['main']['name'])
          print(f"Temperature: {main['temp']}°C")
          print(f"Humidity: {main['humidity']}%")
          print(f"Pressure: {main['pressure']}hPa")
          print(f"weather: {weather[0]['description']}")
          print(f"Wind Speed: {wind['speed']}m/s")

if __name__ == '__main__':
     city = input("Enter City Here: ")
     weather_data = get_weather(city)
     display_weather(weather_data)

#OR
# import requests

#api_key = "df030222f78e01e08300ebf7b1441f04"
#user_input = input("Enter city: ")

#data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}")

#print(data.json())
#if data.json()['cod'] == '404':
#     print("Not City found")
#else:
#     weather = data.json()['weather'][0]['main']
#     temp = round(data.json()['main']['temp'])
#     humidity = data.json()['main']['humidity']

#     print(f"The weather in {user_input} is: {weather}")
#     print(f"The temperature in {user_input} is: {temp}°F")
#     print(f"The humidity in {user_input} is: {humidity}")