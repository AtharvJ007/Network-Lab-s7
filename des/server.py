import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def decrypt_message(key, ciphertext):
    cipher = Cipher(algorithms.DES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(ciphertext) + decryptor.finalize()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Server listening on port 12345")

    connection, address = server_socket.accept()
    print(f"Connection from {address}")

    key = input("Enter the DES key (8 characters): ").encode('utf-8')

    while True:
        ciphertext = connection.recv(1024)
        if not ciphertext:
            break

        decrypted_message = decrypt_message(key, ciphertext)
        print(f"Received message: {decrypted_message.decode('utf-8')}")

    connection.close()

if __name__ == "__main__":
    start_server()

