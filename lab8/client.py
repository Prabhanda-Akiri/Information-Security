import socket
import sys

s = socket.socket()
s.connect(("10.50.3.172",9999))
f = open ("test.txt", "rb")
l = f.read(1024)

while (l):
    s.send(l)
    l = f.read(1024)
s.close()