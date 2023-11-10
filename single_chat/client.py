import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)

# Connect to the server
client_socket.connect(server_address)

try:
    input_string = input("Enter a string: ")
    client_socket.send(input_string.encode())

    # Receive the length of the string from the server
    string_length = client_socket.recv(1024).decode()
    print(f"Length of the string received from server: {string_length}")
except socket.error as err:
    print(f"Socket error: {err}")
finally:
    # Close the socket
    client_socket.close()

