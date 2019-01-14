# -*- coding: utf-8 -*-
"""
Socket client for practice

Created on Fri Jan  4 11:50:57 2019

@author: ANSHAY
"""

import socket
import sys

try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("could not create socket")
    mysock.close()
    sys.exit()
print("mysock socket created")

try:
    host = socket.gethostbyname("www.google.com")
    print("host: " + host)
except socket.error:
    print("could not find host")
    mysock.close()
    sys.exit()

try:
    mysock.connect((host, 80))
except socket.error:
    print("could not connect")
    mysock.close()
    sys.exit()
print ("connection established")

message = b"GET / http/1.1\r\n\r\n"
mysock.sendall(message)
data = mysock.recv(1000)
print(data)
mysock.close()
