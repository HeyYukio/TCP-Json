import json
import socket

settings = {
    'host': '127.0.0.1',
    'port': 9091
}

def create_tcp_connection():
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((settings['host'], settings['port']))
        server_socket.listen(1)
        print(f'Aguardando conexão ...') 
        client_socket, addr = server_socket.accept()
        return server_socket, client_socket
        
    except socket.error as e:
        print(f'Falha ao se conectar com {settings["host"]}:{settings["port"]}')
        print(e)
        return None
    
def receive_data(client_socket):

    print(f'Aguardando dados ...')
    data = client_socket.recv(1024)
    json_data = data.decode('utf-8').split('/n')[0]
    data = json.loads(json_data)
    print(f'Dados recebidos: {data}')

while True:
    server_socket = None 
    client_socket = None
    server_socket, client_socket = create_tcp_connection()
    while True:
        try:
            receive_data(client_socket)
        except Exception as e:
            print('Falha no recebimento do json')
            print(e)
            server_socket.close()
            client_socket.close()
            break

