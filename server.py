"""
*********************************************************
*                                                       *
* Project Name: Socket Squares                     *
* Author: github.com/kirigaine                          *
* Description: A simple socket project with pygame,     *
*   each player controls a randomly generated square    *
*   and can see eachother's movement.                   *
* Requirements: TBD                                     *
*                                                       *
*********************************************************
"""
import socket
import threading
#import pickle
#import square as sq

# Append player to square when join

# Server network constants
SERVERIP = socket.gethostbyname(socket.gethostname())
PORT = 26256

# Server data constraints
HEADER = 16
FORMAT = 'utf-8'

# Create and bind server socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVERIP,PORT))

# Create array of player squares
player_squares = []
#testsquare = sq.Square()
#print(testsquare.name)
#player_squares.append(testsquare)


def clientHandling(client_conn, client_addr):
    # Boolean to manage connection status for server
    connected = True
    print(f"[SERVER] Connection established @ {client_addr[0]}:{PORT}")

    while connected:

        # Receive header that describes data length
        data_length = client_conn.recv(HEADER).decode(FORMAT)

        # If data has any content/exists, process the data
        if data_length:
            # Convert the header to an integer to use to receive exact amount of data
            data_length = int(data_length)
            data = client_conn.recv(data_length).decode(FORMAT)
            # If data is specific message, disconnect client
            if data == "!disconnect":
                connected = False
                print(f"{client_addr} has disconnected")
            # Print data if not attempt to disconnect
            else:
                print (f"[{client_addr}] says: {data}")
            # Send confirmation message to client
            client_conn.send("Data received".encode(FORMAT))

    # Disconnect client
    client_conn.close()

    

def serverLaunch():
    # Start socket listening
    print("[SERVER] Server is launching...")
    server.listen()
    print(f"[SERVER] Server is listening at {SERVERIP} on port {PORT}")

    while True:
        # If a client attempts to connect, accept and store connection and address
        client_conn, client_addr = server.accept()
        # Create a thread and pass method to handle client
        thread = threading.Thread(target=clientHandling, args=((client_conn,client_addr)))
        thread.start()
        #print(f"[SERVER] Current Users: {threading.activeCount() - 1}")
        #with client_conn:
            #while True:
               # data = client_connection.recv(1024)
                #if not data:
                #    break
                #client_connection.sendall(data)

serverLaunch()