import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 65432        # Port to listen on

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print("Server is listening...")

# Accept a connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    # Receive data from the client
    data = conn.recv(1024)  # Buffer size: 1024 bytes
    if not data:
        break
    print(f"Received: {data.decode()}")

    # Process the data and send a response
    response = f"Server received: {data.decode()}"
    conn.sendall(response.encode())

conn.close()
