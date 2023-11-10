import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define the server address and port
host = '127.0.0.1'
port = 12345

# Bind the socket to the server address and port
server_socket.bind((host, port))

print("Socket is listening...")

while True:
    # Receive the string from the client
    input_data, client_address = server_socket.recvfrom(1024)
    input_string = input_data.decode()
    
    if input_string.lower() == "exit":
        print("Received 'exit' from client. Closing server.")
        server_socket.close()
        break
    else:
        # Reverse the string
        reversed_string = input_string[::-1]

        # Send the reversed string back to the client
        server_socket.sendto(reversed_string.encode(), client_address)

