# import socket library 
import socket

# import threading library 
import threading

# Choose a port that is free 
PORT = 5050

# An IPv4 address is obtained 
# for the server.    
SERVER = socket.gethostbyname(socket.gethostname())

# Address is stored as a tuple 
ADDRESS = (SERVER, PORT)

# the format in which encoding 
# and decoding will occur 
FORMAT = "utf-8"

# Lists that will contains 
# all the clients connected to  
# the server and their names. 
clients, names = [], []

# Create a new socket for 
# the server  
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# bind the address of the  
# server to the socket  
server.bind(ADDRESS)


# function to start the connection
def startChat():
    print("[INFO] Starting server...\n[INFO] Server address is: " + SERVER)

    # listening for connections  
    server.listen()

    while True:
        # accept connections and returns
        # a new connection to the client 
        #  and  the address bound to it  
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))

        # 1024 represents the max amount 
        # of data that can be received (bytes)
        try:
            name = conn.recv(1024).decode(FORMAT)
            ip = conn.recv(1024).decode(FORMAT)
        except ConnectionResetError:
            name = ''
            ip = ''

        # Check if name and ip has been received, else deny
        if len(name) > 1 and len(ip) > 1:

            # Check if name already exists
            name_accepted = True
            for checkname in names:
                if name == checkname:
                    name_accepted = False
                    name = ''
                    ip = ''
                    conn.send("Name already exists.".encode(FORMAT))
            if name_accepted:
                conn.send("Name accepted".encode(FORMAT))

            # append the name and client
            # to the respective list
            names.append(name)
            clients.append(conn)

            # broadcast join message
            broadcastMessage(f"{name} has joined the chat!".encode(FORMAT), conn)

            # Start the handling thread
            thread = threading.Thread(target=handle,
                                      args=(conn, addr, ip, name))
            thread.start()

            # no. of clients connected
            # to the server
            print(f"[INFO] Current active connections: {threading.activeCount() - 1}")
        else:
            print("[WARNING] Connection outside of client was blocked.")
    # method to handle the


# incoming messages
def handle(conn, addr, ip, name):
    print(f"[INFO] New connection from: {ip}\n")
    connected = True

    while connected:
        # receive message
        message = conn.recv(1024).decode(FORMAT)
        if message == "#Close connection#":
            connected = False
        else:
            # broadcast message
            broadcastMessage(message.encode(FORMAT))

    # close the connection
    print("Connection closed.")
    clients.remove(conn)
    names.remove(name)
    conn.close()


# method for broadcasting
# messages to the each clients
def broadcastMessage(message, conn=None):
    for client in clients:
        if client != conn:
            client.send(message)

# call the method to
# begin the communication
startChat()
