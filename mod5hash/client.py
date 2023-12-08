import socket

def decrypt(encrypted_message):
    # Simple decryption for demonstration purposes
    decrypted_message = ''.join(chr(ord(char) - 1) for char in encrypted_message)
    return decrypted_message

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'
port = 12345
client_socket.connect((host, port))

# Receive the MD5 hash from the server
md5_hash_received = client_socket.recv(1024).decode('utf-8')

# Display the received MD5 hash
print(f"MD5 Hash received from server: {md5_hash_received}")

# Close the connection
client_socket.close()

