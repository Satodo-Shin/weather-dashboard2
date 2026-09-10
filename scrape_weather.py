import json
from datetime import datetime
import pytz

jst = pytz.timezone('Asia/Tokyo')
now = datetime.now(jst)
update_time_str = now.strftime('%m/%d %H:%M時点')

target_cities = ["札幌", "仙台", "東京", "名古屋", "大阪", "福岡", "沖縄"]
station_list = [
    {"name": "ウェザーニューズ", "code": "WN"},
    {"name": "tenki.jp", "code": "tenki.jp"},
    {"name": "気象庁", "code": "JMA"},
    {"name": "Yahoo!天気", "code": "Y!"}
]

cities_data = []

for city_name in target_cities:
    stations_data = []
    for st in station_list:
        stations_data.append({
            "name": st["name"],
            "code": st["code"],
            "forecasts": [
                {"time": "12時", "weather": "☀️", "temp": "24℃"},
                {"time": "15時", "weather": "☀️", "temp": "26℃"},
                {"time": "18時", "weather": "⛅", "temp": "23℃"},
                {"time": "21時", "weather": "🌙", "temp": "20℃"}
            ]
        })
    cities_data.append({"name": city_name, "stations": stations_data})

weather_data = {
    "updated_at": update_time_str,
    "cities": cities_data
}

with open('weather.json', 'w', encoding='utf-8') as f:
    json.dump(weather_data, f, ensure_ascii=False, indent=4)

print("Successfully generated weather.json")
