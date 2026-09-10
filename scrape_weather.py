import json
from datetime import datetime
import pytz

# 現在の日本時間を取得
jst = pytz.timezone('Asia/Tokyo')
now = datetime.now(jst)
update_time_str = now.strftime('%m/%d %H:%M時点')

# ダッシュボード用のダミー/初期データ構造（自動スクレイピングの組み込み拡張用）
# 今後各サイトのパーサーをここに追加してデータを自動生成します
weather_data = {
    "updated_at": update_time_str,
    "stations": [
        {"name": "ウェザーニューズ", "code": "WN", "temp_12": "24℃", "temp_15": "25℃", "temp_18": "22℃"},
        {"name": "日本気象協会", "code": "tenki.jp", "temp_12": "25℃", "temp_15": "24℃", "temp_18": "22℃"},
        {"name": "気象庁", "code": "JMA", "temp_12": "24℃", "temp_15": "23℃", "temp_18": "21℃"},
        {"name": "Yahoo!天気", "code": "Y!", "temp_12": "24℃", "temp_15": "23℃", "temp_18": "21℃"}
    ]
}

# weather.jsonファイルとして書き出し
with open('weather.json', 'w', encoding='utf-8') as f:
    json.dump(weather_data, f, ensure_ascii=False, indent=4)

print("Weather data updated successfully at", update_time_str)
