from websocket_server import WebsocketServer
from operator import add, mul, sub,truediv, floordiv
from functools import reduce
 
def new_client(client, server): # clientと接続したときにメッセージを出力
  print('New client %s:%s has joined.' % (client['address'][0], client['address'][1]))
  
def client_left(client, server): # clientとの接続が切れたときにメッセージを出力
  print('This client %s:%s has left.\n' % (client['address'][0], client['address'][1]))

def message_received(client, server, message): # 受け取ったメッセージから四則演算し、結果を返す
  print('%s have been received from %s:%s' % (message, client['address'][0], client['address'][1]))
  s = list(map(float, message.split())) # 空白を含む文字列を数値に変換しリスト作成
  sum = str(reduce(lambda x, y: x+y, s)) # 和を求める
  sub = str(reduce(lambda x, y: x-y, s)) # 差を求める
  mul = str(reduce(lambda x, y: x*y, s)) # 積を求める
  if (0 in s[1:]): # 先頭以外に0があるときのみ例外処理
    div = 'error'
  else:
    div = str(reduce(lambda x, y: x/y, s)) # 商を求める
  reply_message = '\n 和: ' + sum + '\n 差: ' + sub + '\n 積: ' + mul + '\n 商: ' + div + '\n'
  server.send_message(client, reply_message) # clientに計算結果を返す
 
# Main
if __name__ == "__main__":
  server = WebsocketServer(port=12345, host='127.0.0.1') # サーバーの設定
  server.set_fn_new_client(new_client) # clientと接続したときに呼ぶ関数を指定
  server.set_fn_client_left(client_left) # clientとの接続が切れたときに呼ぶ関数を指定
  server.set_fn_message_received(message_received) # clientからメッセージを受け取ったときに呼ぶ関数を指定
  server.run_forever() # websocketサーバーを起動
