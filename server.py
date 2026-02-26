import socket

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

# Receive and echo messages
while True:
    prompt = ["Some prompt or whatever ____", "Hello", "Goodbye", "See you later", "Alighty"]
    client.send(prompt.encode())

    msg = client.recv(1024).decode()
    if not msg:
        break
    print(f"Received: {msg}")
    client.send(f"Server received: {msg}".encode())

client.close()
server.close()