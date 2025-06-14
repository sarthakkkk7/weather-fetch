from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("❗ ERROR: API_KEY not found. Check your .env file.")
    exit()

def get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        print(f"\nWeather in {city.title()}:\n")
        print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
        print(f"☁️ Condition: {weather}")
        print(f"💧 Humidity: {humidity}%")
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        print(f"🌧️ Rain: {data.get('rain', {}).get('1h', 0)} mm in the last hour")
    else:
        print(f"\n❌ Error: {response.status_code} — {response.json().get('message', 'Unknown error')}")

if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    get_weather(city_name)
