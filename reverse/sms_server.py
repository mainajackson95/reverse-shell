#!/usr/bin/python
import socket

imarkelam = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
imarkelam.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
imarkelam.bind(("192.168.100.12",54321))
imarkelam.listen(5)
print("Listening for Incoming connections!")
target, ip = imarkelam.accept()
print("Target Connected!")
while True:
    message = raw_input("* HackerOne#~%s " % str(ip))
    target.send(message)
    if message == "q":
        break
    else:
        answer = target.recv(1024)
        print(answer)
imarkelam.close()
