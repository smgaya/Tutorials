# Thomas Reaney
# Electronic & Computer Engineering Student
# National University of Ireland Galway

import socket

host = ""
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as ex:
    print(ex)

s.listen(5)

conn, addr = s.accept()

print("Connected to: " + addr[0] + ":" + str(addr[1]))

"""
- Go to cmd.exe
- telnet localhost 5555
"""