import socket
from cryptography.fernet import Fernet

# Clave generada, asegúrate de usar la misma que en el servidor
key = b'B0rd9z6V40ze4WDmG7rlsh5GnR9Eaok1c4NoOS3b5Xc='
cipher_suite = Fernet(key)

# Configuración del cliente
HOST = '192.168.0.221'
PORT = 60000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    command = input("Ingrese un comando (o /.-Exit para salir): ")
    
    client_socket.send(command.encode())
    
    if command == "/.-Exit":
        print("Cerrando la conexión del cliente.")
        break
    
    encrypted_response = client_socket.recv(4096)
    response = cipher_suite.decrypt(encrypted_response).decode()
    print(response)

client_socket.close()
