# 🌦️ Weather App (Python + OpenWeatherMap API)

A simple Python project that fetches real-time weather data from OpenWeatherMap API and displays temperature, humidity, wind speed, rainfall (in last hour) and weather conditions for a given city.

## 🔧 Features:
- Secure API key handling via `.env`
- Uses `requests` to make HTTP calls
- Parses JSON response and presents data
- Basic error handling included
- Text-to-speech functionality. 

## 🛠 Requirements:
- Python 3.x
- `requests`
- `python-dotenv`
- `pyttsx3`

## 🚀 Setup & Run
```bash
pip install -r requirements.txt
python main.py
```

## 📁 File Structure:
- `main.py` — Main logic
- `.env` — Your API key (add your own!)
- `requirements.txt` — Dependencies
- `.gitignore` — Prevents `.env` from uploading

## ✅ Output Example:
```
Enter a city name: Khopoli

Weather in Khopoli:

🌡️ Temperature: 25.18°C (Feels like 26.29°C)
☁️ Condition: moderate rain
💧 Humidity: 97%
💨 Wind Speed: 4.98 m/s
🌧️ Rain: 1.62 mm in the last hour

Thank you for using the Weather App!🙏🏼
```

📌 *Note:* Get your API key from https://openweathermap.org/api and put it inside `.env` like:
```
API_KEY=your_api_key_here
```
🐞Incase of failure in functioning of API Key:
 
  Debug by placing following code in main.py below ''response = requests.get(base_url, params=params)'' :-


    print("Request URL:", response.url)  # Debug
   
    print("Response Content:", response.text)  # Debug
    

## ✨Feedback:

  If any suggestions keep it to yourself man!🤺

  It was built just for Practice purpose 🏋️‍♂️

  Just kidding! Suggestions are always appreciated.

  Will try to enhance it further.🪄

## 👨‍💻 Author:
[Sarthak Deshmukh](https://github.com/sarthakkkk7)
