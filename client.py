#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket, sys

try:
	
    SERVER = sys.argv[1]
    PORT = int(sys.argv[2])
    LINE = ' '.join(sys.argv[3:])

except:

    sys.exit("Usage client.py ip puerto register sip_address expires_value")


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, PORT))
    print("Enviando:", LINE)
    Words = LINE.split(" ")
    MSG = Words[0]
    DIRECCION = Words[1]
    EXPIRES = int(Words[2])
    print(DIRECCION)
    if MSG == "register":
        Mensaje = ("REGISTER sip:" + DIRECCION + "SIP/2.0\r\n")
        LINE = Mensaje
        my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
