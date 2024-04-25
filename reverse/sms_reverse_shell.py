#!/usr/bin/python
import socket

ramimalek = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ramimalek.connect(("192.168.100.12",54321))
print("Connection Established To Server")
while True:
    message = ramimalek.recv(1024)
    print(message)
    if message == "q":
        break
    else:
        message_back = raw_input("Type Message To Send To Server: ")
        ramimalek.send(message_back)
ramimalek.close()
