# Crystal-Method-kadai


## 課題内容
画面から数字を入力し、webソケット通信を用いて四則演算の結果を返す。

## 開発環境
Python 3.6.5 :: Anaconda, Inc.

## 実行方法
始めに、以下のモジュールをインストールする。  
・サーバー側  
`$ sudo pip install git+https://github.com/Pithikos/python-websocket-server`  
・クライアント側  
`$ sudo pip install websocket-client`  

次にコマンドプロンプト上で以下を実行する。  
・サーバー側  
`$ python server.py`  
・クライアント側  
`$ python client.py`

最後に、計算したい数値をクライアント側で空白で区切って入力し、エンターキーで決定すれば、四則演算の結果が返る。

## 実行例

・sever側  
`$ python server.py`  
clientと接続後  
`New client 127.0.0.1:64017 has joined`  
clientで数字を読み込んだ後  
`2 2 have been received from 127.0.0.1:64017`  
`This client 127.0.0.1:64017 has left.'`  

・client側  
`$ python client.py`  
```
数字を空白で区切って入力し、エンターキーで決定してください。  
2 2  
Received '  
 和: 4.0  
 差: 0.0  
 積: 4.0  
 商: 1.0  
'  
Close
```
