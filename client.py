from websocket import create_connection

ws = create_connection("ws://127.0.0.1:12345") # サーバーのIPアドレスとポート番号を設定し、サーバーに接続
print("数字を空白で区切って入力し、エンターキーで決定してください。")
i = input() # 計算する数値を入力
ws.send(i) # サーバーにその数値を送る
result = ws.recv() # サーバーから結果を受け取る
print("Received '%s'" % result) # 計算結果を出力
ws.close() # サーバーとの接続を切る
print("Close")
