import requests


class bybitapi:
    base_url = "https://api.bybit.com"  # Базовый URL для всех запросов

    def make_request(self, endpoint, params=None):
        response = requests.get(self.base_url + endpoint, params=params)
        result = response.json()
        return result

    def get_orderbook(self, symbol, category):
        endpoint = "/v5/market/orderbook"
        params = {
            'category': category,  # Категория передается c main.py
            'symbol': symbol
        }
        data = self.make_request(endpoint, params)

        return data
