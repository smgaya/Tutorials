# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import socket
import sys
import time


# Create socket
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
    except socket.error as ex:
        print("Socket creation error: " + str(ex))


# Bind socket to port and wait for connection from client
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding socket to port " + str(port))
        s.bind((host, port))
        # Allows server to accept connections
        # Number of bad connections = 5
        s.listen(5)
    except socket.error as ex:
        print("Socket binding error: " + str(ex) + "\nRetrying.....")
        time.sleep(5)
        bind_socket()


# Establish a connection with client (socket must be listening for them)
def accept_socket():
    conn, address = s.accept()
    print("Connection has been established | " + address[0] + " | Port " + str(address[1]))
    send_commands(conn)
    conn.close()


# Send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


def main():
    create_socket()
    bind_socket()
    accept_socket()

main()
