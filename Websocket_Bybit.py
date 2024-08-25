# Убедитесь, что библиотека websocket-client установлена: pip install websocket-client
import json
import traceback
import websocket
import threading


class Socket_conn_Bybit(websocket.WebSocketApp):
    def __init__(self, url, params=None):
        super().__init__(
            url=url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        self.params = params
        self.run_forever(ping_interval=15, ping_timeout=10)

    def on_open(self, ws):
        print(ws, 'Websocket was opened')
        # Подписка на топики:
        if self.params is not None:
            data = {"op": "subscribe", "args": self.params}
            ws.send(json.dumps(data))

    def on_error(self, ws, error):
        print('on_error', ws, error)
        print(traceback.format_exc())
        exit()

    def on_close(self, ws, status, msg):
        print('on_close', ws, status, msg)
        exit()

    def on_message(self, ws, msg):
        data = json.loads(msg)
        print(data)


# URL
url = "wss://stream.bybit.com/v5/public/linear"

# топики для подписки
topic = [
    "kline.1.AXSUSDT",
    "kline.1.SOLUSDT",
    "orderbook.1.AXSUSDT",
    "orderbook.1.SOLUSDT"
]
# не работает!!
# threading.Thread(target=Socket_conn_Bybit, args=(url, topic)).start()

thread = threading.Thread(target=Socket_conn_Bybit, args=(url, topic))
thread.start()
thread.join()
