
import socket 
import json
import time

settings = {
    'host': '127.0.0.1',
    'port': 9091
}

data = {
    'category': 'Test',
    'name': "Henrique Yukio Murata",
    'counter': 1
}

def create_tcp_connection():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((settings['host'], settings['port']))
        print(f'Conectado a {settings["host"]}:{settings["port"]}')
        return client_socket
    except socket.error as e:
        print(f'Falha ao se conectar com {settings["host"]}:{settings["port"]}')
        print(e)
        return None

def sendData(client_socket):
    try:
        json_data = json.dumps(data)
        encoded_json = (json_data+'\n').encode('utf-8')
        client_socket.send(encoded_json)
        print('Envio do json por UDP bem sucedido')
        data['counter'] = data['counter'] + 1
        time.sleep(5)
        
    except socket.error as e:
        print(['Falha ano envio do json por UDP'])
        print(e)
        client_socket.close()
        create_tcp_connection()
        
client_socket = None
client_socket = create_tcp_connection()
while True:
    sendData(client_socket)



