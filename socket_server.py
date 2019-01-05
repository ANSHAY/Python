# -*- coding: utf-8 -*-
"""
a simple socket server for practice
Created on Fri Jan  4 12:06:11 2019

@author: ANSHAY
"""

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind(("", 1234))
mysock.listen(5)
while True:    
    conn, addr = mysock.accept()
    data = conn.recv(1000)
    if not data:
        break
    print(data)
    conn.sendall(data)
    conn.close()
mysock.close()
