from dotenv import load_dotenv
import os
import requests
import pyttsx3
import time
from colorama import init, Fore, Style

init(autoreset=True)

engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

print("Choose your preferred voice:")
speak("Choose your preferred voice.")
print("1. Male 👨")
engine.say("Option one - Male voice.")
engine.runAndWait()
print("2. Female 👩")
engine.say("Option two - Female voice.")
engine.runAndWait()
voice_choice = input("Enter 1 or 2: ")


# Set voice based on user preference
voices = engine.getProperty('voices')
if voice_choice == "1":
    engine.setProperty('voice', voices[0].id)  # Male
    print("You have selected Male Voice.\n")
    speak("Hello! You have selected male voice.")
else:
    engine.setProperty('voice', voices[1].id)  # Female
    print("You have selected Female Voice.\n")
    speak("Hello! You have selected female voice.")

# Set properties for speech
engine.setProperty('rate', 180)  # Set speech rate
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
# Function to return emoji based on weather description
def get_weather_emoji(description):
    desc = description.lower()
    if "clear" in desc:
        return "☀️"
    elif "cloud" in desc:
        return "☁️"
    elif "rain" in desc:
        return "🌧️"
    elif "thunder" in desc:
        return "⛈️"
    elif "snow" in desc:
        return "❄️"
    elif "mist" in desc or "fog" in desc:
        return "🌫️"
    elif "drizzle" in desc:
        return "🌦️"
    else:
        return "🌡️"

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
        print(Fore.LIGHTWHITE_EX + f"{time.strftime('%I:%M %p')} ")
        engine.say(f"As of {time.strftime('%I:%M %p')} ")
        engine.runAndWait()
        print(Fore.YELLOW + f"\nThe Weather in {city.title()}:\n")
        engine.say(f"Weather in {city.title()}:")
        engine.runAndWait()
        print(Fore.RED + f"🌡️  Temperature: {temp}°C (Feels like {feels_like}°C)")
        engine.say(f"Temperature is {temp}°C")
        engine.runAndWait()
        emoji = get_weather_emoji(weather)
        print(f"{emoji}  Condition: {weather}")
        engine.say(f"Condition is {weather}")
        engine.runAndWait()
        print(Fore.LIGHTCYAN_EX + f"💧 Humidity: {humidity}%")
        engine.say(f"Humidity is {humidity}%")
        engine.runAndWait()
        print(Fore.LIGHTGREEN_EX + f"💨 Wind Speed: {data['wind']['speed']} m/s")
        engine.say(f"Wind Speed is {data['wind']['speed']} metres per second")
        engine.runAndWait()
        print(Fore.BLUE + f"🌧️  Rain: {data.get('rain', {}).get('1h', 0)} mm in the last hour")
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
    city_name = input(Fore.LIGHTMAGENTA_EX + "Enter a city name 🌆 : ")
    get_weather(city_name)



