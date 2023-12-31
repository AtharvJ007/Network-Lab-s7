import socket
import threading

def receive_messages(client_socket):
    try:
        while True:
            message = client_socket.recv(1024).decode()
            print(message)
    except:
        print("Disconnected from the server.")
        client_socket.close()
        exit()

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('127.0.0.1', 12345)

try:
    # Connect to the server
    client_socket.connect(server_address)

    # Get the client name
    client_name = input("Enter your name: ")
    client_socket.send(client_name.encode())

    # Start a thread to receive messages
    threading.Thread(target=receive_messages, args=(client_socket,)).start()

    # Send messages to the server
    while True:
        message = input()
        client_socket.send(message.encode())
except:
    print("An error occurred.")
finally:
    # Send an exit message and close the socket
    client_socket.send("exit".encode())
    client_socket.close()

