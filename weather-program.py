# Author: Miles Peña
# Date: 11/18/2023

import requests

def get_api_key():
    return input("Enter your OpenWeather API key: ")

def get_location_city(app_id):
    city = input("Please enter city name: ")
    state = input("Please enter state code: ")
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city},{state},us&limit=1&appid={app_id}&units=imperial"
    response = requests.get(url)
    res = response.json()
    lat = res[0]['lat']
    lon = res[0]['lon']
    name = res[0]['name']
    return lat, lon, name

def get_location_zip(app_id):
    zip_code = input("Please enter zip code: ")
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},us&appid={app_id}&units=imperial"
    response = requests.get(url)
    res = response.json()
    lat = res['lat']
    lon = res['lon']
    name = res['name']
    return lat, lon, name

def get_weather(lat, lon, app_id):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={app_id}&units=imperial"
    response = requests.get(url)
    res = response.json()
    name = res['name']
    temp = res['main']['temp']
    feels_like = res['main']['feels_like']
    high_temp = res['main']['temp_max']
    low_temp = res['main']['temp_min']
    pressure = res['main']['pressure']
    humidity = res['main']['humidity']
    description = res['weather'][0]['description']
    print(f'\nThe current temperature in {name} is: {temp}°F')
    print(f'Feels Like: {feels_like}°F')
    print(f'High Temp: {high_temp}°F')
    print(f'Low Temp: {low_temp}°F')
    print(f'Pressure: {pressure} hPa')
    print(f'Humidity: {humidity}%')
    print(f'Description: {description}\n')

def main():
    print('Welcome to the Weather Program!')
    app_id = get_api_key()

    while True:
        try:
            user_answer = input("Type 'city' for city/state, 'zip' for zip code, or 'q' to quit: ")
            if user_answer.lower() == "q":
                print("Thank you for using the weather app!")
                break
            elif user_answer.lower() == "zip":
                lat, lon, name = get_location_zip(app_id)
                get_weather(lat, lon, app_id)
            elif user_answer.lower() == "city":
                lat, lon, name = get_location_city(app_id)
                get_weather(lat, lon, app_id)
            else:
                print("Please enter a valid response.")
        except (ValueError, IndexError):
            print("We couldn't retrieve the location. Please try again.")
        except requests.exceptions.RequestException as error:
            print(f"Network error: {error}")
            break

if __name__ == "__main__":
    main()
