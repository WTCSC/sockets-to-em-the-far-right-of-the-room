import socket

def connect():    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = input("Please input the server ip: ")

    try:
        client.connect((server_ip, 5000))
        print("Connected to server")
        player_id = client.recv(1024).decode()

        while True:
            received = client.recv(1024).decode()
            print(f"The prompt is \"{received[0]}\"")
            hand = recieved[player_id]

            msg = input("Enter message: ")
            if not msg:
                break
            client.send(msg.encode())
            response = client.recv(1024).decode()
            print(f"Server says: {response}")

        client.close()




        #except ValueError:
        #    print("The port you inputted wasn't an integer. Please reinput the server ip and port.\n")
        #    continue

    except ConnectionRefusedError:
        print("Wasn't able to connect, please try again.\n")

    except:
        client.close()
        print("Some error occured, please try again\n")
    
    finally:
        client.close()


def send_msg():
    while True:
        msg = input("Enter message: ")
        if not msg:
            break
        client.send(msg.encode())
        response = client.recv(1024).decode()
        print(f"Server says: {response}")

    client.close()

connect()