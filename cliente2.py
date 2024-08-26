import socket
import struct
import random

def mine_block(block):
    nonce = random.randint(0, 2**64 - 1)
    # Aqui você pode implementar a lógica de hash para validar o nonce com o bloco.
    # Para este exemplo, apenas retornamos o nonce.
    return nonce

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))
    
    # Recebe o bloco de dados do servidor
    block = client.recv(1024)
    
    # Inicia o processo de mineração
    nonce = mine_block(block)
    
    # Envia o nonce encontrado de volta ao servidor
    client.send(struct.pack('Q', nonce))
    
    # Recebe a resposta do servidor
    response = client.recv(1024)
    print(response.decode("utf-8"))

if __name__ == "__main__":
    start_client()
