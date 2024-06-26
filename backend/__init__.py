CLIENT_CONNECTS_TO_STR = "wss://localhost:12345"
# CLIENT_CONNECTS_TO_STR = "wss://7.tcp.eu.ngrok.io:18059"
# ^ This should always be in wss format, for example wss://7.tcp.eu.ngrok.io:18059

SERVER_ADDR_TUPLE = ('localhost', 12345)

SERVER_HLS_HOST, SERVER_HLS_PORT = 'localhost', 8000
CLIENT_HLS_HOST, CLIENT_HLS_PORT = 'localhost', 8000
# CLIENT_HLS_HOST, CLIENT_HLS_PORT = '0.tcp.eu.ngrok.io', 14347


SERVER_CRT_PATH = r"../certificate/server.crt"
SERVER_KEY_PATH = r"../certificate/server.key"