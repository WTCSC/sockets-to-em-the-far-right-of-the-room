import socket
from time import sleep

# Create a socket object (IPv4 + TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to 0.0.0.0:5000
server.bind(("0.0.0.0", 5000))

# Listen for connections
server.listen(1)
print("Waiting for connection...")

# Accept client connection
client, addr = server.accept()
print(f"Connected to {addr}")
msg = "4"
client.send(msg.encode())
recieved = client.recv(1024).decode()

# Receive and echo messages
while True:
    prompt = "Some prompt or whatever | 5.12.6.43.1 | 7.23.25.3.53 | 41.40.15.27.2 | 18.16.35.20.40"
    client.send(prompt.encode())

    msg = client.recv(1024).decode()
    if not msg:
        break
    print(f"Received: {msg}")
    client.send(f"Server received: {msg}".encode())
    sleep(1)

client.close()
server.close()