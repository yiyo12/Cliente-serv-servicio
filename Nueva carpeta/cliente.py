#!/usr/bin/env python
# -*- coding: utf-8 -*-
from socket import socket
from time import time
import packet
# Compatibilidad con Python 3 
try:
    raw_input
except NameError:
    raw_input = input
def main():
    s = socket()
    s.connect(("localhost", 3030))
    while True:
        message = raw_input("Manda algo al servidor> ")
        print("Justo despues de mter en el input "+message)

        if message.lower() == "ping":
            output_data = packet.pack(packet.PING, "")
            ticks = time()
        else:
            output_data = packet.pack(packet.MESSAGE, message[1:]) 
            print("Mensaje del message[1:] en cliente"+output_data)
        #elif message.lower() == 'servicio':
           #output_data = packet.pack(packet.MESSAGE, message[1:])
          
        
        packet.send(s, output_data)
        print("impresion del cliente del outData"+output_data)
        incoming_data = s.recv(1024)
        print("impresion del cliente del incoData"+incoming_data)
        
        if incoming_data:
            packet_id, message = packet.unpack(incoming_data)
            if packet_id == packet.MESSAGE:
                if isinstance(message, bytes):
                    print("asasas"+message)
                    message = message.decode("utf-8")
                    print("Mensaje con decode"+message)
                #print("El servidor ha respondido: %s." % message)
                if message == 'servicio':
                    import ConOpenCv
                    pass
                print("Este mensaje es "+message)
            elif packet_id == packet.PING:
                ticks = (time() - ticks) / 2
                print("Ping: %.2f ms." % ticks)
    
    s.close()
if __name__ == "__main__":
    main()
