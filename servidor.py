import socket
import struct
import threading

HOST = 'localhost'
PORT = 12345

nonce_encontrado = None
lock = threading.Lock()

def handle_client(conn, addr):
    global nonce_encontrado
    print(f'Cliente conectado: {addr}')

    conn.sendall(b'Pronto para receber o nonce.')

    data = conn.recv(1024)
    nonce = struct.unpack('i', data)[0]

    with lock:
        if nonce_encontrado is not None:
            conn.sendall('Nonce já encontrado.'.encode('utf-8'))
        else:
            nonce_encontrado = nonce
            conn.sendall(b'Nonce aceito!')

    print(f'Cliente {addr} enviou nonce: {nonce}')
    conn.close()

if __name__ == '__main__':
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f'Servidor ouvindo em {HOST}:{PORT}')

        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr)).start()
