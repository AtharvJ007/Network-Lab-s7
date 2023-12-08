import socket

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8080))

    message = input("Enter a message to send to the server: ")
    client.send(message.encode('utf-8'))

    decrypted_response = client.recv(1024).decode('utf-8')
    #print("Decrypted response from server:", decrypted_response)

    client.close()

if __name__ == "__main__":
    main()
