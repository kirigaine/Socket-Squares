"""
client.py
"""
import socket
import re
import pygame
#import square

# Server network
user_input = ""

# Determine if given IPv4 is "valid" using regex
x = None
while not x:
    user_input = input("\nEnter the IPv4 Address of a server to connect to: ")
    x = re.search("^[0-9]{1,3}\.{1}[0-9]{1,3}\.{1}[0-9]{1,3}\.{1}[0-9]{1,3}$", user_input)
    if not x:
        print("Invalid IPv4. Please try again following the format: X.X.X.X")


SERVERIP = user_input
PORT = 26256

# Server data constraints
HEADER_SIZE = 16
FORMAT_TYPE = 'utf-8'

# Create and connect client socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVERIP,PORT))
print(f"[SERVER] You have connected to the server @ {SERVERIP}")
#print("Received from server: " + repr(data))

def sendData(data):
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

# Initialize and manage pygame settings
#pygame.init()
#pygame.display.set_caption("Socket Squares Test")

# Declare pygame screen
#screen = pygame.display.set_mode((800,600))

# Send two test inputs to server
myinput = ""
while myinput != "exit":
    myinput = input("Say: ")
    sendData(myinput)
