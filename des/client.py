import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_message(key, message):
    cipher = Cipher(algorithms.DES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    return encryptor.update(message) + encryptor.finalize()

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    key = input("Enter the DES key (8 characters): ").encode('utf-8')

    while True:
        message = input("Enter a message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        ciphertext = encrypt_message(key, message.encode('utf-8'))
        client_socket.send(ciphertext)

    client_socket.close()

if __name__ == "__main__":
    start_client()

