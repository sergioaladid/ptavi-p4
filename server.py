#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver, sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
 
    Dicc = {}

    def handle(self):
       
        self.wfile.write(b"Hemos recibido tu peticion")
        mensaje = line.decode('utf-8')
        print("El cliente nos manda: ", mensaje)
        
        for line in self.rfile:
            Direccion = msg[msg.find("sip:") + 4 : msg.rfind(" SIP/2.0")]
            Expires = int(msg[msg.find("Expires: ") + 9 : msg.find("\r\n\r\n")])
            Dir_Ip = self.client_address[0]
            mensaje = line.decode('utf-8')
        
            if Expires == 0:
                del self.Dicc[Direccion]
				
            elif Expires > 0:
                self.Dicc[Dir] = {'address': Dir_Ip, 'Expires': Expires}
            print(Dicc)
			
            self.wfile.write(b"SIP/2.0 200 OK\r\n\r\n")

if __name__ == "__main__":
    
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler) 
    print("Lanzando servidor UDP de eco...")
    
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
