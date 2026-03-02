import socket
import threading

# Create a socket object (IPv4 + TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to 0.0.0.0:5000
server.bind(("0.0.0.0", 5000))

#server sends out prompt to all clients and they must catch it
#clients send in their cards
#server sends out everyones played cards to everyone
#clients send in votes 
#server returns winner
#repeat
clients_num = 0
start = False

prompt = "_"

ans = []

def parse_msg(client, name, message):
    global start
    words = message.split()
    match words[0]:
        case "play":
            ans.append(message.split("play")[1])
        case "draw":
            #draw a card and send it to the player
            client.send()
        case "vote":
            #vote on card
            client.send()
        case "prompt":
            client.send(prompt.encode())
        case "start":
            #start the game
            print("start")
            start = True
            #client.send("recieved".encode())
        case _:
            client.send(f"unknown message starter {words[0]}".encode())
            print(f"recived unknown message from client {name}: {message}")


#read client inputs
def read_client(client, name):
    global clients_num
    while True:
        msg = client.recv(1024).decode()
        if not msg:
            break
        parse_msg(client, name, msg)
        client.send("ok".encode())
    #reduce clients when someone leaves
    #clients_num -= 1
    print(f"client {name} left")
    clients_num -= 1
    client.close()
    

clients = []


while not start:
    print(start)
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

#tell clients to start
for client in clients:
    client.send("start".encode())

#get prompt 
prompt = "ok"

while len(ans) < clients_num:
    _ = 0

pack = ""

for answer in ans:
    pack.append(f"\n\n{answer}")

for client in clients:
    client.send(pack.encode())

server.close()