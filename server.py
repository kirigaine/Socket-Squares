"""
*********************************************************
*                                                       *
* Project Name: Socket Squares                          *
* Author: github.com/kirigaine                          *
* Description: A simple socket project with pygame,     *
*   each player controls a randomly generated square    *
*   and can see eachother's movement.                   *
* Requirements: pip install -r requirements.txt         *
*                                                       *
*********************************************************
"""
import socket
import threading
from queue import Queue
import pickle
#from random import randint

import square as sq

# Server network constants
SERVERIP = socket.gethostbyname(socket.gethostname())
PORT = 26256
MAX_USERS = 8

# Server data constraints
HEADER_SIZE = 16
FORMAT_TYPE = 'utf-8'

# Create and bind server socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((SERVERIP,PORT))

player_squares = [None,None,None,None,None,None,None,None]
pos_updates = Queue()
ps_lock = threading.Lock()
q_lock = threading.Lock()

def clientHandling(client_conn, client_addr, new_square):
    # Boolean to manage connection status for server
    connected = True

    print("[THREAD] Acquiring the ps_lock...")
    with ps_lock:
        print("[THREAD] ps_lock acquired. Appending square.")
        player_squares[new_square.player_id-1] = new_square
    print("[THREAD] Released the ps_lock.")

    new_square = pickle.dumps(new_square)
    theader_data = f"{len(new_square):<{HEADER_SIZE}}"
    client_conn.send(theader_data.encode(FORMAT_TYPE))
    client_conn.send(new_square)

    print(f"[SERVER] Connection established @ {client_addr[0]}:{PORT}")
    while connected:

        # Receive header that describes data length
        header_data = client_conn.recv(HEADER_SIZE).decode(FORMAT_TYPE)

        # If data has any content/exists, process the data
        if header_data:
            # Convert the header to an integer to use to receive exact amount of data
            header_data = int(header_data)
            # Receive exact square object data from player
            data = pickle.loads(client_conn.recv(header_data))
            # Place square into queue to be handled, then reset for next iteration
            
            with q_lock:
                pos_updates.put(data)
            header_data = data = ""

            # Send the current state of player_squares to client
            current_list = pickle.dumps(player_squares)
            aheader_data = f"{len(current_list):<{HEADER_SIZE}}"
            client_conn.send(aheader_data.encode(FORMAT_TYPE))
            client_conn.send(current_list)


    # Disconnect client
    client_conn.close()

def queueHandling():
    while True:
        if not pos_updates.empty():
            current_it = None
            c_id = None

            with q_lock:
                current_it = pos_updates.get()
                c_id = current_it.player_id
            with ps_lock:
                player_squares[c_id-1] = current_it
            


def serverLaunch():
    # Start socket listening
    print("[SERVER] Server is launching...")

    # Limit total amount of clients connected
    server.listen(8)
    print(f"[SERVER] Server is listening at {SERVERIP} on port {PORT}")

    # Create factory for squares that gives distinct id's square to player
    sq_factory = sq.SquareFactory()

    # Create thread to handle queue
    q_thread = threading.Thread(target=queueHandling)
    q_thread.start()

    # Server listening for clients loop
    while True:
        # If a client attempts to connect, accept and store connection and address
        client_conn, client_addr = server.accept()
        # Create a thread and pass method to handle client
        thread = threading.Thread(target=clientHandling, args=((client_conn,client_addr,sq_factory.createSquare())))
        thread.start()
        # Display current amount of users when someone connects
        print(f"[SERVER] Current Users: {threading.activeCount() - 2}/{MAX_USERS}")



serverLaunch()