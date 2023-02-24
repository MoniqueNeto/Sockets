import socket
import random

# Define endereço IP e porta do servidor
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 5000

# Define o número de números a serem gerados
NUMBERS_TO_GENERATE = 1000

# Cria socket TCP do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
client_socket.connect((SERVER_ADDRESS, SERVER_PORT))

# Gera e envia números aleatórios ao servidor
number = 1
for i in range(NUMBERS_TO_GENERATE):
    delta = random.randint(1, 100)
    number += delta
    message = str(number).encode()
    client_socket.sendall(message)
    print("Produtor enviou o número:", number)
    
    # Aguarda resposta do servidor
    data = client_socket.recv(1024).decode()
    print("Produtor recebeu a resposta:", data)

# Envia mensagem de encerramento
message = '0'.encode()
client_socket.sendall(message)

# Fecha conexão
client_socket.close()

