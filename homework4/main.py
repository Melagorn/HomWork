import hashlib
import hmac
import json
import time
import requests
from config import API_KEY, SECRET_KEY
from binance import Binance_api

# Данная функция будет создавать сигнатуру из отправленных в нее params (в формате словаря)
def gen_signature(params):
    param_str = '&'.join([f'{k}={v}' for k, v in params.items()])
    signature = hmac.new(bytes(SECRET_KEY, "utf-8"), param_str.encode("utf-8"), hashlib.sha256).hexdigest()
    return signature

api = Binance_api(futures=True)
futuer_tickers = api.get_price_ticker(symbol="AXSUSDT")
price = futuer_tickers["price"]
price_up  = float(price) + (float(price) * 0.5)
price_down = float(price) - (float(price) * 0.5)
print(price, price_up, price_down)


#order_bay = api.post_limit_order(symbol="AXSUSDT", side="BUY", qnt = 1, price = price_up)
#order_sell = api.post_limit_order(symbol="AXSUSDT", side="SELL", qnt = 1, price = price_down)
# 1 Базовая ссылка + ендпоинт:
url = "https://fapi.binance.com/fapi/v1/order"

# 2. Заголовки:
header = {
    "X-MBX-APIKEY": API_KEY
}

# 3 Параметры:
timestamp = int(time.time() * 1000)

params = {
    "symbol": "AXSUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 2,
    "price": price_up,
    "timestamp": timestamp,
}

params2 = {
    "symbol": "AXSUSDT",
    "side": "SELL",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 2,
    "price": price_down,
    "timestamp": timestamp,
}


# 4 Сигнатура:
params['signature'] = gen_signature(params)
params2['signature'] = gen_signature(params2)




# 5 Отправка запроса:
new_order_buy = requests.post(url=url, params=params, headers=header).json()
new_order_sell = requests.post(url=url, params=params2, headers=header).json()

print(new_order_buy, new_order_sell)
