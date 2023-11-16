import logging
from websocket_server import WebsocketServer

def new_client(client, server):
	print(client)
	print("Client(%d)" % (client['id']))
	server.send_message_to_all("Hey all, a new client has joined us")

def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))
	#server.send_message(client, message)
	server.send_message_to_all(message)

server = WebsocketServer(host='127.0.0.1', port=13254, loglevel=logging.INFO)
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.run_forever()
