import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('127.0.0.1', 12345)

try:
    input_string = input("Enter a string: ")
    client_socket.sendto(input_string.encode(), server_address)

    if input_string.lower() == "exit":
        print("Client exiting...")
    else:
        # Receive the reversed string from the server
        reversed_string_data, _ = client_socket.recvfrom(1024)
        reversed_string = reversed_string_data.decode()
        print(f"Reversed string received from server: {reversed_string}")
except socket.error as err:
    print(f"Socket error: {err}")
finally:
    # Close the socket
    client_socket.close()

