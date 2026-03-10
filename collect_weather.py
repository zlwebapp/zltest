"""
Collect Shanghai daily weather. Run once per day (e.g. cron).
Uses Open-Meteo API (no API key). Appends one record to shanghai_weather_daily.json.
"""
import json
import os
from datetime import datetime

import requests

SHANGHAI_LAT = 31.23
SHANGHAI_LON = 121.47
URL = "https://api.open-meteo.com/v1/forecast"
OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "shanghai_weather_daily.json")


def collect():
    params = {
        "latitude": SHANGHAI_LAT,
        "longitude": SHANGHAI_LON,
        "current_weather": "true",
        "timezone": "Asia/Shanghai",
    }
    r = requests.get(URL, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    today = datetime.now().strftime("%Y-%m-%d")
    record = {
        "date": today,
        "collected_at": datetime.now().isoformat(),
        "temperature": data["current_weather"].get("temperature"),
        "windspeed": data["current_weather"].get("windspeed"),
        "winddirection": data["current_weather"].get("winddirection"),
        "weathercode": data["current_weather"].get("weathercode"),
    }
    records = []
    if os.path.exists(OUTPUT_FILE):
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            records = json.load(f)
    records.append(record)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    return record


if __name__ == "__main__":
    print(collect())
