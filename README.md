# 🌦️ Weather App (Python + OpenWeatherMap API)

A simple Python project that fetches real-time weather data from OpenWeatherMap API and displays temperature, humidity, wind speed, rainfall (in last hour) and weather conditions along with the time of weather report for a given city.
![17507019288017904972910296204142](https://github.com/user-attachments/assets/1c941224-7ab7-42dc-b934-ee3418d38d72)


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
### 🔊Voice Preference:
```
Choose your preferred voice:
1. Male 👨
2. Female 👩
Enter 1 or 2: 1
You've selected Male Voice.
```
### 🌍Weather details:
```
Enter a city name 🌆: Khopoli
As of 23:02:42

The Weather in Khopoli:

🌡️ Temperature: 25.45°C (Feels like 26.37°C)
☁️ Condition: broken clouds
💧 Humidity: 89%
💨 Wind Speed: 1.75 m/s
🌧️ Rain: 0 mm in the last hour

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
