import socket
import struct
import random

# Configurações do cliente
HOST = 'localhost'
PORT = 12345

def minerar_nonce():
    # Simulação do processo de mineração
    nonce = random.randint(0, 1000000)
    print(f'Nonce gerado: {nonce}')
    return nonce

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        # Recebe a mensagem inicial do servidor
        s.recv(1024)

        # Gera um nonce
        nonce = minerar_nonce()

        # Envia o nonce para o servidor
        data = struct.pack('i', nonce)
        s.sendall(data)

        # Recebe a confirmação do servidor
        resposta = s.recv(1024)
        print(f'Resposta do servidor: {resposta.decode()}')

if __name__ == '__main__':
    start_client()
