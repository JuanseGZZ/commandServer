from cryptography.fernet import Fernet

# Genera una clave válida
key = Fernet.generate_key()

# Imprime la clave en formato base64 (cópiala y úsala en ambos lados)
print(key.decode())
