import socket
from cryptography.fernet import Fernet
import subprocess

# Clave generada, asegúrate de usar la misma en el cliente
key = b'B0rd9z6V40ze4WDmG7rlsh5GnR9Eaok1c4NoOS3b5Xc='
cipher_suite = Fernet(key)

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 60000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)
print(f"Esperando conexiones en {HOST}:{PORT}...")

client_socket, addr = server_socket.accept()
print(f"Conexión entrante de {addr[0]}:{addr[1]}")

while True:
    command = client_socket.recv(1024).decode()
    
    if command == "/.-Exit":
        print("Cliente ha enviado /.-Exit. Cerrando conexión.")
        break
    
    try:
        # Ejecutar el comando en la consola y capturar la salida
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
    except Exception as e:
        result = str(e)

    # Encripta y envía la salida al cliente
    encrypted_result = cipher_suite.encrypt(result.encode())
    client_socket.send(encrypted_result)

client_socket.close()
server_socket.close()
