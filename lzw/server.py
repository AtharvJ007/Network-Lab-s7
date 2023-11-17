import socket

def encode_data(data):
    table = {chr(i): i for i in range(256)}
    p = data[0]
    code = 256
    output_code = []
    
    print("String\tOutput_Code\tAddition")
    i = 0
    while i < len(data):
        if i != len(data) - 1:
            c = data[i + 1]
        if p + c in table:
            p = p + c
        else:
            output_code.append(table[p])
            print(f"{p}\t{table[p]}\t\t{p + c}\t{code}")
            table[p + c] = code
            code += 1
            p = c
        c = ""
        i += 1
    
    output_code.append(table[p])
    print(f"{p}\t{table[p]}")
    return output_code

def start_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()

        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024).decode()
                encoded_data = encode_data(data)
                print(f"Encoded Data: {encoded_data}")
                conn.sendall(','.join(map(str, encoded_data)).encode())
                print("Encoding completed")
                conn.close()

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 12345
    start_server(HOST, PORT)
