import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
host = '127.0.0.1'
port = 12345

# Bind the socket to the server address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print("Socket is listening...")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Receive the string from the client
    input_string = client_socket.recv(1024).decode()
    
    if input_string == "exit":
        print("Received 'exit' from client. Closing server.")
        server_socket.close()
        break
    else:
        # Get the length of the string
        string_length = str(len(input_string))

        # Send the length of the string back to the client
        client_socket.send(string_length.encode())

    # Close the client socket
    client_socket.close()

