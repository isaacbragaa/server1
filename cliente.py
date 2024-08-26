import socket
import struct
import random

HOST = 'localhost'
PORT = 12345

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        s.recv(1024)  # Recebe a mensagem inicial do servidor

        nonce = random.randint(0, 1000000)
        print(f'Nonce gerado: {nonce}')

        s.sendall(struct.pack('i', nonce))  # Envia o nonce para o servidor

        resposta = s.recv(1024)
        print(f'Resposta do servidor: {resposta.decode()}')

if __name__ == '__main__':
    main()
