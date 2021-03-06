# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "pythonprogramming.net"


def port_scan(port):
    try:
        s.connect((server, port))
        return True
    except Exception as ex:
        return False

for x in range(1, 30):
    if port_scan(x):
        print("Port ", x, " is open!")
    else:
        print("Port ", x, " is closed!")
