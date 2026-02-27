import socket

def connect():    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = input("Please input the server ip: ")

    try:
        client.connect((server_ip, 5000))
        print("Connected to server")
        player_id = int(client.recv(1024).decode())
        print(f"{player_id}\n")
        hello = 'Hello'
        client.send(hello.encode())
        print(f"Your player id is {player_id}")

        while True:
            received = client.recv(1024).decode().split(' | ')
            print(f"The prompt is \"{received[0]}\"\n")
            hand = received[player_id]
            print(f"Your hand is {hand}")

            msg = input("Enter message: ")
            if not msg:
                break
            client.send(msg.encode())
            response = client.recv(1024).decode()
            print(f"{response}\n")

        client.close()




        #except ValueError:
        #    print("The port you inputted wasn't an integer. Please reinput the server ip and port.\n")
        #    continue

    except ConnectionRefusedError:
        print("Wasn't able to connect, please try again.\n")

    except Error as e:
        client.close()
        print(f"The error '{e}' occured, please try again\n")
    
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

#def print_hand(hand):
#    number = 1
#    with open("answers.txt") as file:
#        for card in hand.split('.'):
#            card_text = file.read().split('\n')[18]
#            print(f"{number}) {card_text}")
#            number += 1
#        print(file.read().split('\n'))
#    return True
#
#
##connect()
#
#print_hand('18.16.35.20.40')