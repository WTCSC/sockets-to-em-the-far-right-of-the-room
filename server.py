import socket
import threading

# Create a socket object (IPv4 + TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to 0.0.0.0:5000
server.bind(("0.0.0.0", 5000))

#amount of clients currently connected to the server
clients_num = 0
start_votes = 0


def parse_msg(client, name, message):
    words = message.split()
    print("ok cool")

#read client inputs
def read_client(client, name):
    while True:
        msg = client.recv(1024).decode()
        if not msg:
            break
        parse_msg(client, name, msg)
    #reduce clients when someone leaves
    client.close()
    clients_num -= 1

clients = []

while start_votes < clients_num or clients_num < 2:
    # Listen for connections
    server.listen(1)
    print("Waiting for connection...")

    # Accept client connection
    client, addr = server.accept()
    print(f"Connected to {addr}")

    clients_num += 1
    # Receive and echo messages
    t = threading.Thread(target=read_client, args=(client, clients_num, ))
    t.start()
    clients.append(client)


server.close()