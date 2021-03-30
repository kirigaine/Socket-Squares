"""
client.py
"""
import socket
import pygame
#import square

# Server network
SERVERIP = input("Enter IP Address to connect to: ")
PORT = 26256

# Server data constraints
HEADER = 16
FORMAT = 'utf-8'

# Create and connect client socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((SERVERIP,PORT))
print(f"[SERVER] You have connected to the server @ {SERVERIP}")
#print("Received from server: " + repr(data))

def sendData(data):
    # Encode string in utf-8
    alldata = data.encode(FORMAT)

    # Determine length of data to send as header
    data_length = len(alldata)

    # Encode data length string in utf-8 and add buffer
    send_length = str(data_length).encode(FORMAT)
    send_length += b' ' * (HEADER-len(send_length))

    # Send header to server, then data
    client.send(send_length)
    client.send(alldata)

    # Receive data from server
    print(client.recv(2048).decode(FORMAT))

# Initialize and manage pygame settings
pygame.init()
pygame.display.set_caption("Socket Squares Test")

# Declare pygame screen
screen = pygame.display.set_mode((800,600))

# Send two test inputs to server
print("Say: ",end='')
sendData(input())
sendData("!disconnect")
