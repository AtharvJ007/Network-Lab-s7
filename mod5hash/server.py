import socket
import hashlib

def encrypt(message):
    # Simple encryption for demonstration purposes
    encrypted_message = ''.join(chr(ord(char) + 1) for char in message)
    return encrypted_message

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

# Accept a connection from a client
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")

# Get user input for the message
message_to_send = input("Enter a message: ")

# Encrypt the message
encrypted_message = encrypt(message_to_send)

# Calculate the MD5 hash of the encrypted message
md5_hash = hashlib.md5(encrypted_message.encode('utf-8')).hexdigest()

print(f"Original Message: {message_to_send}")
print(f"Encrypted Message: {encrypted_message}")
print(f"MD5 Hash of Encrypted Message: {md5_hash}")

# Send the MD5 hash to the client
client_socket.send(md5_hash.encode('utf-8'))

# Close the connection
client_socket.close()

