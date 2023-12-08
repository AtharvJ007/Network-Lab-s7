import socket

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a' ) + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A' ) + shift) % 26 + ord('A'))
        else:
            result += char
    return result

def handle_client(client_socket):
    data = client_socket.recv(1024).decode('utf-8')
    shift = 3  # You can change the shift value as needed

    # Encryption on the server side
    encrypted_data = caesar_cipher(data, shift)
    print("Encrypted data on server:", encrypted_data)

    # Decryption on the server side
    decrypted_data = caesar_cipher(encrypted_data, -shift)
    print("Decrypted data on server:", decrypted_data)

    client_socket.send(decrypted_data.encode('utf-8'))
    client_socket.close()

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 8080))
    server.listen(5)
    print("[*] Listening on 127.0.0.1:8080")

    while True:
        client, addr = server.accept()
        print("[*] Accepted connection from: %s:%d" % (addr[0], addr[1]))
        handle_client(client)

if __name__ == "__main__":
    main()
