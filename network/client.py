import socket

# Server configuration
HOST = '127.0.0.1'  # Server's hostname or IP address
PORT = 65432        # Port to connect to

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

while True:
    # Get user input
    message = input("Enter your move (e.g., 'move up'): ")
    if message.lower() == 'quit':
        break

    # Send the message to the server
    client_socket.sendall(message.encode())

    # Receive the server's response
    data = client_socket.recv(1024)
    print(f"Server says: {data.decode()}")

client_socket.close()
