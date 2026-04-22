import requests
import os

# === ① 抓股價 ===
stock_url = "https://query1.finance.yahoo.com/v8/finance/chart/2303.TW"
headers = {
    "User-Agent": "Mozilla/5.0"
}

res = requests.get(stock_url, headers=headers)
data = res.json()

price = data['chart']['result'][0]['meta']['regularMarketPrice']

# === ② 從環境變數讀取 ===
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

message = f"聯電目前股價：{price}"

telegram_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
payload = {
    "chat_id": CHAT_ID,
    "text": message
}

requests.post(telegram_url, data=payload)

print("已發送:", message)
