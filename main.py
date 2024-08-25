from Api_Bybit import bybitapi


def find_largest_spread(api, trading_pairs, category):
    largest_spread = 0
    largest_spread_pair = None

    for pair in trading_pairs:
        # Получаем данные ордербука для каждой пары
        data = api.get_orderbook(pair, category)

        # Извлекаем лучший аск и бид из данных
        best_bid = float(data['result']['b'][0][0])  # Первая цена в списке бидов
        best_ask = float(data['result']['a'][0][0])  # Первая цена в списке асков

        # Вычисляем спред
        spread = best_ask - best_bid
        print(f"Пара: {pair}, Бид: {best_bid}, Аск: {best_ask}, Спред: {spread}")

        # Сравниваем текущий спред с наибольшим
        if spread > largest_spread:
            largest_spread = spread
            largest_spread_pair = pair

    return largest_spread_pair, largest_spread


if __name__ == '__main__':
    api = bybitapi()

    # Список из 10 любых торговых пар
    trading_pairs = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "LTCUSDT", "EOSUSDT",
                     "BCHUSDT", "DOTUSDT", "ADAUSDT", "XLMUSDT", "LINKUSDT"]

    category = "linear"
    # Ищем пару с самым большим спредом для указанной категории
    largest_spread_pair, largest_spread = find_largest_spread(api, trading_pairs, category)
    print(f"Пара с самым большим спредом: {largest_spread_pair}, Спред: {largest_spread}")
