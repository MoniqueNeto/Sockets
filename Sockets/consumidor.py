import socket
import math

# Define endereço IP e porta do servidor
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 5000

# Cria socket TCP do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Vincula o socket a um endereço IP e porta
server_socket.bind((SERVER_ADDRESS, SERVER_PORT))

# Entra em modo de escuta
server_socket.listen()

# Aguarda conexão do cliente
print("Consumidor aguardando conexão...")
client_socket, client_address = server_socket.accept()
print("Cliente conectado:", client_address)

# Recebe e processa números enviados pelo produtor
while True:
    data = client_socket.recv(1024).decode()
    number = int(data)
    
    # Verifica se o número é primo
    if number <= 1:
        is_prime = False
    elif number <= 3:
        is_prime = True
    elif number % 2 == 0 or number % 3 == 0:
        is_prime = False
    else:
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                is_prime = False
                break
            i += 6
        is_prime = True
    
    # Verifica se o número é par ou ímpar
    if number % 2 == 0:
        is_even = True
    else:
        is_even = False
    
    # Envia resposta ao produtor
    response = ''
    if is_prime:
        response += 'Primo '
    else:
        response += 'Não Primo '
    if is_even:
        response += 'Par'
    else:
        response += 'Ímpar'
    message = response.encode()
    client_socket.sendall(message)
    print("Consumidor recebeu o número:", number, "e enviou a resposta:", response)
    
    # Encerra conexão caso seja recebido o número 0
    if number == 0:
        break

# Fecha conexão
client_socket.close()
server_socket.close()
