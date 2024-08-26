servidor master possui uma msg(teste) um bloco de mineração em hash
cliente pergunta se tem algum tipo de validação
servidor responde que tem 3 bytes zero antes

for i in range (0, 10000000):
  s=hashlib.sha256()
  s.update(strict.pack("I", i)+b'vitorialeticia')
  s.hexdigest()
  input(str(i)+''+a)


PROTOCOLO: usando structs (como calcular o nonce?)
G + nome do minerador(10 bytes)   cliente -> servidor (pedido de transferencia p minerar)
T + numero da transação(2 bytes) + numero do minerador(2bytes) + sugestão de tamanho de slot de mineração(4bytes) bits zeros nonce(1byte) + tamanho da transação(2bytes) + dados da transações(2bytes)  servidor -> cliente  (retorno de transação para minerar)
S + numero da transação(2 bytes) + nonce(4bytes)  cliente -> servidor (sucesso encontrou o nonce)
A + numero da transação(2 bytes)  servidor -> cliente (notificação de validação ao vencedor de que o nonce foi validado)
I + numero da transação(2 bytes)  servidor -> cliente (invalida transação por nonce ter sido encontrado)
R + numero da transação(2 bytes)  servidor -> cliente (notifica o falso vencedor de que o nonce não confere)
Q + servidor -> cliente (msg de gentileza fim da operação)

cliente, um servidor
servidor gera 1024 bytes 
cliente request bytes ao servidor
tenta encontrar o nonce
quando encontrar notifica o servidor
recebe uma msg do servidor que alguém minerou já aquele byte e então para


usando threads cliente conecta no servidor e pede transações(gera um conjunto de bytes), então servidor fornece. O cliente2 pede transações e o servidor fornece. é preciso achar o nonce desse conjunto de bytes



faça um código em python usando struct, thread e hashlib

Servidor:

Gera um bloco de transações: O servidor cria um novo bloco de transações, que é um conjunto de transações que precisam ser processadas e adicionadas à blockchain.
Aguarda requisições de clientes: O servidor aguarda que os clientes se conectem e solicitem o bloco de transações.
Verifica se alguém já minerou o bloco: Quando um cliente notifica que encontrou o nonce, o servidor verifica se alguém já minerou aquele bloco. Se sim, o servidor rejeita a notificação e aguarda que outro cliente encontre o nonce.
Envia confirmação para o cliente: Se ninguém ainda minerou o bloco, o servidor envia uma confirmação para o cliente que encontrou o nonce, indicando que o bloco foi minerado com sucesso.

Cliente:

Conecta-se ao servidor: O cliente se conecta ao servidor para solicitar um bloco de transações.
Solicita um bloco de transações: O cliente solicita um bloco de transações ao servidor.
Inicia o processo de mineração: O cliente inicia um processo de mineração para encontrar o nonce daquele bloco. Isso envolve tentar diferentes combinações de números até encontrar uma que atenda ao desafio criptográfico.
Notifica o servidor: Assim que o cliente encontra o nonce, ele notifica o servidor.



É importante notar que, em um sistema de mineração de criptomoedas real, existem muitos outros fatores envolvidos, como:

A dificuldade do desafio criptográfico é ajustada periodicamente para manter a taxa de mineração constante.
Os clientes precisam ter uma cópia da blockchain para verificar a validade das transações.
