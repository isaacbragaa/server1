import socket
import threading
import struct

# Bloco de dados a ser minerado
BLOCK_SIZE = 1024
nonce_found = False
block = bytearray(BLOCK_SIZE)

def handle_client(client_socket, client_address):
    global nonce_found

    try:
        # Envia o bloco de dados para o cliente
        client_socket.send(block)
        
        # Aguarda o cliente enviar o nonce encontrado
        data = client_socket.recv(8)  # Tamanho do nonce esperado (64 bits)
        if len(data) == 8:
            received_nonce = struct.unpack('Q', data)[0]
            print(f"Cliente {client_address} encontrou nonce: {received_nonce}")
            
            if not nonce_found:
                nonce_found = True
                client_socket.send("Sucesso! Bloco minerado.".encode('utf-8'))
            else:
                client_socket.send("Falha! Outro cliente já minerou o bloco.".encode('utf-8'))
        else:
            client_socket.send("Dados inválidos.".encode('utf-8'))
    finally:
        client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Servidor aguardando conexões...")

    while True:
        client_socket, client_address = server.accept()
        print(f"Conexão recebida de {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_handler.start()

if __name__ == "__main__":
    start_server()
