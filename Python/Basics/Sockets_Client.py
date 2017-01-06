# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import socket
from _thread import *

host = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as ex:
    print(ex)

s.listen(5)
print("Waiting for a connection....")


def threaded_client(conn):
    conn.send(str.encode("\nWelcome! value your information"))

    while True:
        data = conn.recv(2048)
        reply = "\nServer output: " + data.decode("utf-8")
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: " + addr[0] + ":" + str(addr[1]))

    start_new_thread(threaded_client, (conn,))
