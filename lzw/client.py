import socket

def decode_data(encoded_data):
    table = {i: chr(i) for i in range(256)}
    old = encoded_data[0]
    s = table[old]
    c = s[0]
    decoded_data = s
    
    count = 256
    for i in range(len(encoded_data) - 1):
        n = encoded_data[i + 1]
        if n not in table:
            s = table[old] + c
        else:
            s = table[n]
        
        decoded_data += s
        c = s[0]
        table[count] = table[old] + c
        count += 1
        old = n
    
    return decoded_data

def start_client(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        
        user_input = input("Enter the string to be encoded: ")
        client_socket.sendall(user_input.encode())

        encoded_data_str = client_socket.recv(1024).decode()
        encoded_data = list(map(int, encoded_data_str.split(',')))

        decoded_data = decode_data(encoded_data)

        print(f"Original Input: {user_input}")
        print(f"Decoded Output: {decoded_data}")

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 12345
    start_client(HOST, PORT)
