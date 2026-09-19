import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server_socket.bind(("127.0.0.1", 5000))
    server_socket.listen(1)

    print("Server is waiting for a connection...")

    connection, address = server_socket.accept()

    print("Connected to:", address)

    message = connection.recv(1024).decode()

    print("Message received:", message)

    connection.close()

except socket.error as error:
    print("Network error:", error)

finally:
    server_socket.close()