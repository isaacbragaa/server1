import socket
import struct
import threading

# Configurações do servidor
HOST = 'localhost'
PORT = 12345

# Para garantir que o nonce só seja aceito uma vez
nonce_encontrado = None
lock = threading.Lock()

def handle_client(conn, addr):
    global nonce_encontrado
    print(f'Cliente conectado: {addr}')

    # Envia uma mensagem inicial para o cliente
    conn.sendall(b'Pronto para receber o nonce.')

    # Recebe o nonce do cliente
    data = conn.recv(1024)
    nonce = struct.unpack('i', data)[0]  # Desserializa o nonce recebido

    with lock:
        # Verifica se o nonce já foi encontrado
       if nonce_encontrado is not None:
            conn.sendall('Nonce já encontrado por outro cliente.'.encode('utf-8'))
       else:
            nonce_encontrado = nonce
            conn.sendall(b'Nonce aceito!')

    print(f'Cliente {addr} enviou nonce: {nonce}')
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Servidor ouvindo em {HOST}:{PORT}')

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()

if __name__ == '__main__':
    start_server()
