"""
client.py
"""
# Standard library
import socket
import re
import pickle

# Third party
import pygame
#from pygame.sprite import Group

# Local source
import game_functions as gf
import square

# Server port, IPv4 will be prompted
PORT = 26256

# Server data constraints
HEADER_SIZE = 16
FORMAT_TYPE = 'utf-8'

def main():
    server_ip = ipPrompt()

    # Create and connect client socket
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((server_ip,PORT))

    my_square = client.recv(2048)
    my_square = pickle.loads(my_square)
    #print(f"My square's ID is: {my_square.player_id}")

    # Report to client that connection has been established with server
    print(f"[SERVER] You have connected to the server @ {server_ip}")

    # Initialize and manage pygame settings
    pygame.init()
    pygame.display.set_caption("Socket Squares")

    # Declare pygame screen
    screen = pygame.display.set_mode((800,600))

    while True:

       # gf.check_events(screen, player_square)
        #my_square = pickle.dumps(player_square)
        #sendData(my_square)
        #receive data after send
        #gf.update_screen(screen, player_square)



        # Send two test inputs to server
        myinput = ""
        while myinput != "!quit" and myinput != "!q":
            myinput = input("Say: ")
            dataSwap(myinput, client)

        client.close()
        print("You have disconnected from the server. Now exiting...")
        pygame.quit()
        break


def ipPrompt():
    # Prompt user for IPv4, determine if given IPv4 is "valid" using regex. Don't continue until pass regex
    temp_ipv4 = ""
    regex_passed = None
    while not regex_passed:
        temp_ipv4 = input("\nEnter the IPv4 Address of a server to connect to: ")
        regex_passed = re.search("^[0-9]{1,3}\.{1}[0-9]{1,3}\.{1}[0-9]{1,3}\.{1}[0-9]{1,3}$", temp_ipv4)
        if not regex_passed:
            print("Invalid IPv4. Please try again following the format: X.X.X.X")
    return temp_ipv4

def dataSwap(data, client):

    # Encode string in utf-8
    alldata = data.encode(FORMAT_TYPE)

    # Add buffer and encode data length string in utf-8 
    send_length = f"{len(alldata):<{HEADER_SIZE}}"
    send_length = str(send_length).encode(FORMAT_TYPE)

    # Send header to server, then data
    client.send(send_length)
    client.send(alldata)

    # Receive data from server
    print(client.recv(2048).decode(FORMAT_TYPE))

def drawScreen():

    

    player_square = square.Square(screen)
    #player_squares = Group()
    #player_squares.add(square.Square(screen))

main()