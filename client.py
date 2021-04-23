"""
client.py
"""
# Standard library
import socket
import re
import pickle
import sys

# Third party
import pygame

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

    # Report to client that connection has been established with server
    print(f"[CLIENT] You have connected to the server @ {server_ip}")

    # Initialize and manage pygame settings
    print("[CLIENT] Launching game window...")
    pygame.init()
    pygame.display.set_caption("Socket Squares")
    clock = pygame.time.Clock()

    # Declare pygame screen and resolution
    screen = pygame.display.set_mode((800,600))

    # Done
    print("[CLIENT] Receiving character data...")
    header_data = client.recv(HEADER_SIZE).decode(FORMAT_TYPE)
    if header_data:
        header_data = int(header_data)
        
    my_square = client.recv(header_data)
    my_square = pickle.loads(my_square)
    my_square = square.PlayerSquare(my_square, screen)
    print("[CLIENT] Character data received.")

    # List of all current player squares
    player_squares = [None,None,None,None,None,None,None,None]
    clock.tick(60)

    while True:

        gf.check_events(screen, my_square)

        player_squares = pickleSwap(my_square, client)
        
        gf.update_screen(screen, my_square, player_squares)


    else:
        # Exit cleanly
        client.close()
        print("You have disconnected from the server. Now exiting...")
        pygame.quit()
        sys.exit()



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

def printArray(given_array):
    for item in given_array:
        if item is not None:
            pass

def pickleSwap(data, client):

    # Turn coordinates of player square into a tuple, send to server and receive all square updates
    alldata = pickle.dumps((data.center_x, data.center_y))
    send_length = f"{len(alldata):<{HEADER_SIZE}}"
    send_length = str(send_length).encode(FORMAT_TYPE)

    client.send(send_length)
    client.send(alldata)

    squares = client.recv(HEADER_SIZE)
    squares = int(squares)
    squares = client.recv(squares)

    squares = pickle.loads(squares)
    printArray(squares)
    return squares

main()