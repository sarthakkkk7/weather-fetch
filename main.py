from dotenv import load_dotenv
import os
import requests
import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')  # Set voice (change as needed)
engine.setProperty('rate', 150)  # Set speech rate
engine.setProperty('volume', 1)  # Set volume level (0.0 to 1.0)

speak_text = "Welcome to the Weather App! You can check the weather for any city. Please enter the name of the city."
engine.say(speak_text)
engine.runAndWait() 

load_dotenv()
API_KEY = os.getenv("API_KEY")

if not API_KEY:
    print("❗ ERROR: API_KEY not found. Check your .env file.")
    exit()

# Weather App using OpenWeatherMap API
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
        engine.say(f"Weather in {city.title()}:")
        engine.runAndWait()
        print(f"🌡️ Temperature: {temp}°C (Feels like {feels_like}°C)")
        engine.say(f"Temperature is {temp}°C, Feels like {feels_like}°C")
        engine.runAndWait()
        print(f"☁️ Condition: {weather}")
        engine.say(f"Condition is {weather}")
        engine.runAndWait()
        print(f"💧 Humidity: {humidity}%")
        engine.say(f"Humidity is {humidity}%")
        engine.runAndWait()
        print(f"💨 Wind Speed: {data['wind']['speed']} m/s")
        engine.say(f"Wind Speed is {data['wind']['speed']} metres per second")
        engine.runAndWait()
        print(f"🌧️ Rain: {data.get('rain', {}).get('1h', 0)} mm in the last hour")
        engine.say(f"Rain is {data.get('rain', {}).get('1h', 0)} mm in the last hour")
        engine.runAndWait()
        print("\nThank you for using the Weather App!🙏🏼")
        engine.say("Thank you for using the Weather App!")
        engine.runAndWait()
        exit()
    else:
        print(f"\n❌ Error: {response.status_code} — {response.json().get('message', 'Unknown error')}")
        engine.say("Error occurred while fetching the weather data.")
        engine.runAndWait()
        engine.say(f"Error: {response.status_code} — {response.json().get('message', 'Unknown error')}")
        engine.runAndWait()
        exit()

# Main function to run the weather app
if __name__ == "__main__":
    city_name = input("Enter a city name: ")
    get_weather(city_name)
