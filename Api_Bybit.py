import requests


def make_request(endpoint, params=None):
    base_url = "https://api.bybit.com"
    response = requests.get(base_url + endpoint, params=params)
    result = response.json()
    return result


if __name__ == '__main__':
    endpoint_ticker = "/v5/market/tickers"
    params = {
        'category': 'linear',
        'symbol': 'AXSUSDT'
    }
    ticker = make_request(endpoint_ticker, params)
    ticker = ticker['result']['list'][0]
    print("Ticker >>", ticker)
